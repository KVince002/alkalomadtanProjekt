from django.shortcuts import redirect, render, get_object_or_404
from django.template import loader
from django.http import HttpRequest, HttpResponse
from app.forms import *
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned, MiddlewareNotUsed, SuspiciousOperation
from app.models import *
from django.core import serializers

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
    # felhasználó
    felhasznalo = request.user

    template = loader.get_template("app/about.html")
    context = {
        "cim": "Rólunk",
        "felhasznalo": felhasznalo
        }
    return HttpResponse(template.render(context,request))

# állásokat bemutató oldal
def AllasokBemutato(request):
    print("Állások bemutatójának / Allasok(request)")
    # ha nincs bejelentkezve
    felhasznalo = request.user
    template = loader.get_template("app/jobs.html")

    # de ha be van jekentkezve
    allasok =""
    try:
        # ez a Mumka modellből fog az 30 értéket vissza adni listaként
        allasok =Munka.objects.all()[:30]
    except:
        allasok = "Hihetelen de nincs most aktív hirdetés!"

    context = {
        "cim": "Állások bemutató",
        "felhasznalo": felhasznalo,
        "allasok": allasok
        }
    return HttpResponse(template.render(context,request))

# állások oldal
def Allasok(request):
    print("Állaások főoldalja / Allasok(request)")
    # állások keresése az adatbázisból
    allasok =""

    try:
        # ez a Mumka modellből fog az 30 értéket vissza adni listaként
        allasok =Munka.objects.all()[:30]
    except:
        allasok = "Hihetelen de nincs most aktív hirdetés!"

    print(f"allasok végül: {type(allasok)}")

    template = loader.get_template("app/logedJobs.html")
    context = {
        "cim": "Állások",
        "allasok": allasok
        }
    return HttpResponse(template.render(context,request))

# kapcsolat
def Kapcsolat(request):
    template = loader.get_template("app/contact.html")
    context = {
        "cim": "Kapcsolat"
        }
    return HttpResponse(template.render(context,request))

# profil
def Profil(request):
    # ki van bejelentkezve?
    userId = request.user.id
    userUsername = request.user.username
    felhasznalo = request.user
    print(f"Profil(request) - {userUsername}, ({userId})")


    template = loader.get_template("app/profile/profilePage.html")
    context = {
        "cim": "Profilod",
        "felhasznalo":felhasznalo
        }
    return HttpResponse(template.render(context,request))

# profil / meghírdetett munkák
def Profil_MeglevoMunka(request):
    userId = request.user.id
    userUsername = request.user.username
    felhasznalo = request.user
    print(f"Profil_UjMunka(request) - {userUsername} ({userId})")
    
    # munkák visszadása
    munkak = None
    try:
        munkak = list(Munka.objects.filter(publikalo = request.user.id).values())
    except:
        print(traceback.format_exc())
        munkak = None

    # # Javascript ajax lekérdezéshez
    # if request.is_ajax() and request.method=="POST":
    #     print("AJAX Kérelem fogadva")
    #     munkakVissza = serializers.serialize("json", Munka.objects.filter(publikalo = request.user.id))
    #     print("munkakVissza JSON: ", munkakVissza)

    
    template = loader.get_template("app/profile/profilePageAd.html")
    context = {
        "cim": "Profilod",
        "felhasznalo":felhasznalo,
        "munka": munkak
        }
    return HttpResponse(template.render(context,request))

# profil / új munka
def Profil_UjMunka(request):
    ujMunkaForm = None
    felhasznalo = request.user
    if request.POST:
        if request.user.is_authenticated:
            ujMunkaForm = MunkaFrom(request.POST)
            # for filed in ujMunkaForm:
            #     print(filed)
            if ujMunkaForm.is_valid():
                mentendo = ujMunkaForm.save(commit=False)
                mentendo.publikalo = User.objects.get(pk=request.user.id)
                mentendo.save()
                print("Munka mentve!")
                print(mentendo)

                return redirect("ProfilMeglevoMunka")

            else:
                print("invalid form")
                print(ujMunkaForm.errors)
    else:
        ujMunkaForm = MunkaFrom()
    template = loader.get_template("app/profile/profilePagePlus.html")
    context = {
        "cim": "Profilod",
        "felhasznalo":felhasznalo,
        "form":ujMunkaForm,
        }
    return HttpResponse(template.render(context,request))



# profil / jelentkezők megtekintése az adott munkához
def Profil_JelentkezoMegtekinto(request, munka_Id):
    print("Profil_JelentkezoMegtekinto(request, munka_Id) / profil oldalon a munkára jelentkezők megtekintése")
    felhasznalo = request.user
    
    # jelentkezők megtalálása
    munkaraJelentkezok = None
    try:
        munkaraJelentkezok = list(Jelentkezes.objects.select_related("munkaVallalo").values('munkaVallalo__first_name', 'munkaVallalo__last_name', 'munkaVallalo__email', 'bemutatkozas', 'melleklet', 'berigeny', "ido", "id", "munka"))
        print(munkaraJelentkezok[1])
    except:
        print(traceback.format_exc())
        munkaraJelentkezok = None
    
    # visszaad
    template = loader.get_template("app/profile/profilePageAdDownload.html")
    context = {
        "jelentkezok": munkaraJelentkezok,
        "felhasznalo": felhasznalo,
        "cim": "jelentkezők a munkára"
        }
    return HttpResponse(template.render(context,request))

# ez a függvény fogja letölni a jelentkező dokumentumát
def Profil_JelentkezoDokumentLetolto(request, jelentkezes_id):
    print("Profil_JelentkezoDokumentLetolto(request, jelentkezes_id) / profil munkahírdetések oldalon a jelentkezőnél le tudja tölteni az dokumentumot.")
    felhasznalo = request.user

    letoltendo = get_object_or_404(Jelentkezes, id=jelentkezes_id)
    response = HttpResponse(letoltendo.melleklet, content_type='text/plain')
    response['Content-Disposition'] = f'attachment; filename="{letoltendo.melleklet.name}"'
    return response

def Profil_Jelentkezesek(request):
    userId = request.user.id
    userUsername = request.user.username
    felhasznalo = request.user
    print("Profil_Jelentkezesek(request) / a tejelentkezéseid")

    # új kód
    # felhasználó jelentkezésit tároló lista aminek az eleme a dict
    jelentkezesekLista = [ ]
    try:
        jelentkezesekLista =  list(Jelentkezes.objects.select_related("munka").values( 'bemutatkozas', 'berigeny', "ido", "munka__nev"))
        print(jelentkezesekLista[1])
    except Exception as ex:
        print(ex.with_traceback)

    # visszaad
    template = loader.get_template("app/profile/profilePageApplied.html")
    context = {
        "cim": "Profilod - jelentkezések",
        "felhasznalo":felhasznalo,
        "jelentkezesekLista": jelentkezesekLista,
        }
    return HttpResponse(template.render(context,request))

def MunkaMegtekinto(request, munka_Id):
    # munka megkeresése az id alapján
    print(f"MunkaMegtekinto(request, {munka_Id}) / Részletes munka megtekintő")
    # munka ellenőrzése, hogy létezik-e
    eredmeny = ""
    try:
        eredmeny = Munka.objects.get(id=munka_Id)
        # munka megtekintésének rögzítése
        eredmeny.katt = eredmeny.katt+1
        eredmeny.save()
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
            redirect("ProfilJelentkezesek")
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

# kijelentkezés kérelmező
def KijelentkezKerelem(request):
    print(f"KijelenetkezesKerelem(request) / Kijelentkezés kérelem")
    print(f"{request.user.id}-idval rendelkező ({request.user.username}) kijelentkezik")
    logout(request)
    return redirect("Kezdolap")

# regisztráció 💤
def Regisztral(request):
    print("Regisztral(request) / Regisztrálás")
    if request.method == "POST":
        regisztralasForm = Regisztralas(request.POST)
        if regisztralasForm.is_valid():
            felhasznalo = regisztralasForm.save(commit=False)
            felhasznalo.username = felhasznalo.username.lower()
            felhasznalo.save()
            login(request, felhasznalo)
            return redirect("Profil")
    else:
        regisztralasForm = Regisztralas()
    # válasz
    template = loader.get_template("app/auth/register.html")
    context = {
        "cim": "Regisztráció",
        "form": regisztralasForm
        }
    return HttpResponse(template.render(context, request))

# ⚠️
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
            return redirect("Profil")
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