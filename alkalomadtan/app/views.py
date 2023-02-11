from django.shortcuts import redirect, render
from django.template import loader
from django.http import HttpRequest, HttpResponse
from app.forms import *
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from app.models import *
import os

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
    template = loader.get_template("app/jobs.html")
    context = {
        "cim": "Állások"
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
            for filed in ujMunkaForm:
                print(filed)
            
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
    template = loader.get_template("app/ujmunka.html")
    context = {
        "cim": "Profilod",
        "felhasznalo":felhasznalo,
        "form":ujMunkaForm
        }
    return HttpResponse(template.render(context,request))

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