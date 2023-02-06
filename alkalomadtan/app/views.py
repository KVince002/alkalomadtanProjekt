from django.shortcuts import redirect, render
from django.template import loader
from django.http import HttpRequest, HttpResponse
from app.forms import *
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from app.models import *

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
        fileFelForm = JelentkezesForm(request.POST, request.FILES)
        if fileFelForm.is_valid():
            print(feldolgozo)
            feldolgozo = fileFelForm.save(commit=False)
            feldolgozo.munkaVallalo = User.objects.get(id=request.user.id)
            feldolgozo.ido = django.utils.timezone.now
            feldolgozo.save()
            print(feldolgozo)

            fileFelForm.save()
            print("Fájl menteve?")
    else:
        fileFelForm = JelentkezesForm()
    
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