from django.shortcuts import redirect, render
from django.template import loader
from django.http import HttpRequest, HttpResponse
from app.forms import *
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned, MiddlewareNotUsed, SuspiciousOperation
from app.models import *
import os
import sys
import traceback

# Create your views here.
# kezdőlap
def Homepage(request):
    print("Kezdőlap / homepage()")

    # Válaszadó
    template = loader.get_template("app/index.html")
    context = {
        "cim": "Kezdőlap"
        }
    return HttpResponse(template.render(context,request))

# rólonk oldal
def Rolunk(request):
    template = loader.get_template("app/about.html")
    context = {
        "cim": "Rólunk"
        }
    return HttpResponse(template.render(context,request))

# állások oldal
def Allasok(request):
    print("Állaások főoldalja / Allasok(request)")
    # állások keresése az adatbázisból
    allasok =""

    try:
        # ez a Mumka modellből fog az 20 értéket vissza adni listaként
        allasok =Munka.objects.all()[:20]
    except:
        allasok = "Hihetelen de nincs most aktív hirdetés!"

    print(f"allasok végül: {type(allasok)}")

    template = loader.get_template("app/logedJobs.html")
    context = {
        "cim": "Állások",
        "allasok": allasok
        }
    return HttpResponse(template.render(context,request))

# blog
def Blog(request):
    template = loader.get_template("app/blog.html")
    context = {
        "cim": "Blog"
        }
    return HttpResponse(template.render(context,request))

# profil
def Profil(request):
    # ki van bejelentkezve?
    userId = request.user.id
    userUsername = request.user.username
    felhasznalo = request.user
    print(f"Profil(request) - {userUsername}, ({userId})")


    template = loader.get_template("app/auth/profilePage.html")
    context = {
        "cim": "Profilod",
        "felhasznalo":felhasznalo
        }
    return HttpResponse(template.render(context,request))

# profil / új munka
def Profil_UjMunka(request):
    userId = request.user.id
    userUsername = request.user.username
    felhasznalo = request.user
    print(f"Profil_UjMunka(request) - {userUsername} ({userId})")

    if request.POST:
        if request.user.is_authenticated:
            ujMunkaForm = MunkaFrom(request.POST)
            # for filed in ujMunkaForm:
            #     print(filed)
            if ujMunkaForm.is_valid():
                mentendo = ujMunkaForm.save(commit=False)
                mentendo.publikalo = User.objects.get(pk=request.user.id)
                mentendo.save()
                print("Mentve!")
            else:
                print("invalid form")
                print(ujMunkaForm.errors)         
    else:
        ujMunkaForm = MunkaFrom()
    template = loader.get_template("app/auth/profilePageAd.html")

    # munkák visszadása
    munkak = ""
    try:
        munkak = list(Munka.objects.filter(publikalo = request.user.id).values())
    except:
        print(traceback.format_exc())
        munkak = None
    
    context = {
        "cim": "Profilod",
        "felhasznalo":felhasznalo,
        "form":ujMunkaForm,
        "munka": munkak
        }
    return HttpResponse(template.render(context,request))

def Profil_Jelentkezesek(request):
    userId = request.user.id
    userUsername = request.user.username
    felhasznalo = request.user
    print(f"Profil_UjMunka(request) - {userUsername} ({userId})")
    #jelentkezések keresése
    jelentkezesek = []
    try:
        jelentkezesek = list(Jelentkezes.objects.filter(munkaVallalo = userId).values())
        print("jelentkezesek száma: ", len(jelentkezesek))
        print("jelentkezesek típusa: ", type(jelentkezesek))
        print(jelentkezesek)
    except:
        print(traceback.format_exc())
        jelentkezesek = None
    
    #munkák
    munkak = []
    try:
        munkak = list(Munka.objects.all().values())
    except:
        print(traceback.format_exc())
    
    # munkák és jelentkezés
    eredmeny = []
    try:
        for i in jelentkezesek:
            eredmeny.append(list(Munka.objects.filter(id = i["munka_id"]).values()))
            print("Eredmény típusa: \t", type(eredmeny))
            print("Eredmény\n",eredmeny)
    except:
        print(traceback.print_exc())
    
    # visszaad
    template = loader.get_template("app/auth/profilePageApplied.html")
    context = {
        "cim": "Profilod",
        "felhasznalo":felhasznalo,
        "jelentkezesek": jelentkezesek,
        "munkak": munkak,
        "eredmeny":eredmeny
        }
    return HttpResponse(template.render(context,request))    

def MunkaMegtekinto(request, munka_Id):
    # munka megkeresése az id alapján
    print(f"MunkaMegtekinto(request, {munka_Id}) / Részletes munka megtekintő")
    eredmeny = ""
    try:
        eredmeny = Munka.objects.get(id=munka_Id)
    except ObjectDoesNotExist:
        print("Nem található ilyen munka")
        eredmeny = "Nem volt ilyen munka"
    except MultipleObjectsReturned:
        print("Több munka van ezen az Id-n")
        eredmeny = "Több munka van ezen az id-n"
    print(eredmeny)
    print(type(eredmeny))
    print(eredmeny.helye)

    # jelentkezés része
    if request.POST:
        munkaJelentkezes = JelentkezesFormModel(request.POST, request.FILES)
        if munkaJelentkezes.is_valid():
            jelentkezesMento = munkaJelentkezes.save(commit=False)
            jelentkezesMento.munkaVallalo = User.objects.get(id=request.user.id)
            jelentkezesMento.ido = django.utils.timezone.now()
            jelentkezesMento.felhID = str(request.user.id)
            jelentkezesMento.munka = Munka.objects.get(id=munka_Id)
            jelentkezesMento.save()
            print(jelentkezesMento)
            redirect("Kezdolap")
    else:
        munkaJelentkezes = JelentkezesFormModel()


    # visszaad
    template = loader.get_template("app/jobApply.html")
    context = {
        "cim": "Profilod",
        "munka": eredmeny,
        "form": munkaJelentkezes
        }
    return HttpResponse(template.render(context,request))    

# Ez a függvény el lett távolítva, mert ez már meg lett valósítva. Lásd: MunkaMegtekinto(request, munka_id) függvény
# def MunkaJelentkezo(request, munka_Id):
#     # jelentkezés létrehozása
#     jelentkezesPREP = Jelentkezes.objects.create()
#     jelentkezesPREP.munkaVallalo = request.user.id
#     jelentkezesPREP.munka = munka_Id
#     jelentkezesPREP.ido = django.utils.timezone.now()
    
    
#     # visszaad
#     template = loader.get_template("app/teszt/munkamegjl.html")
#     context = {
#         "cim": "Profilod",
#         }
#     return HttpResponse(template.render(context,request))

# kijelentkezés kérelmező
def KijelentkezKerelem(request):
    print(f"KijelenetkezesKerelem(request) / Kijelentkezés kérelem")
    print(f"{request.user.id}-idval rendelkező ({request.user.username}) kijelentkezik")
    logout(request)
    return redirect("Kezdolap") 

# tesztek
# regisztrálás próbája
def tesztRegisztral(request):
    print("⚠️ teszt regisztráció / tesztRegisztral(request)")

    if request.method == "POST":
        # teszt regisztrálás létrehozása
        tesztRegisztraciosLap = Regisztralas(request.POST)

        # valudálás ellenőrzés
        if tesztRegisztraciosLap.is_valid():
            tRL_Ment =  tesztRegisztraciosLap.Mentes()
            #frissen regisztrál felhasználó regisztrálása
            login(request, tRL_Ment)
            return redirect("Kezdőlap")
    else:
        tesztRegisztraciosLap = Regisztralas()
    
    # válasz
    template = loader.get_template("app/teszt/tesztRegisztral.html")
    context = {
        "cim": "⚠️ tesztRegisztrálás",
        "form": tesztRegisztraciosLap
    }
    return HttpResponse(template.render(context,request))

# dokumentum feltöltés
def tesztFileFel(request):
    print("⚠️ teszt file feltöltés / tesztFileFel()")
    if request.POST:
        fileFelForm = JelentkezesFormModel(request.POST, request.FILES)
        for filed in fileFelForm:
                print(filed)
        if fileFelForm.is_valid():
            modelMento = fileFelForm.save(commit=False)
            modelMento.munkaVallalo = User.objects.get(id=request.user.id)
            modelMento.ido = django.utils.timezone.now()
            modelMento.felhId = str(request.user.id)
            print(modelMento.felhId)
            print(type(modelMento.felhId))
            modelMento.save()
        else:
            print("invalid form")
            print(fileFelForm.cleaned_data.get("melleklet"))
            print(fileFelForm.errors.as_text)
            print(fileFelForm.errors.values)
            print(fileFelForm.errors.get)
    else:
        fileFelForm = JelentkezesFormModel(request.FILES)
    
    template = loader.get_template("app/teszt/tesztForm.html")
    context = {
        "cim": "⚠️ fájl fel, jelentkezes form",
        "form": fileFelForm
    }
    return HttpResponse(template.render(context,request))

# teszt bejelentkezés
def tesztBejelentkez(request):
    print("⚠️ teszt bejelentkezés / tesztBejelentkezes()")
    if request.method == "POST":
        beAuth = AuthenticationForm(data=request.POST)
        if beAuth.is_valid():
            print("valid")
            felhasznaloNev = beAuth.cleaned_data.get("username")
            jelszo = beAuth.cleaned_data.get("password")
            felhasznalo = authenticate(email=felhasznaloNev, password=jelszo)
            print(felhasznalo)
            if felhasznalo is not None:
                login(request, felhasznalo)
                print("bejelentkezve: ")
                return redirect("Kezdőlap")
            else:
                print("elbaszodott a bejelentkezes")
    beAuth = AuthenticationForm()

    template = loader.get_template("app/teszt/tesztBejelentkez.html")
    context = {
        "cim": "⚠️ teszt bejelentkezés",
        "form": beAuth
    }
    return HttpResponse(template.render(context, request))