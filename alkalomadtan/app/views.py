from django.shortcuts import render
from django.template import loader
from django.http import HttpRequest, HttpResponse
from app.forms import *
from django.contrib.auth import logout, authenticate, login
from app.models import *

# Create your views here.
# kezdőlap
def homepage(request):
    print("Kezdőlap / homepage()")

    # Válaszadó
    template = loader.get_template("app/home.html")
    context = {
        "cim": "Kezdőlap"
        }
    return HttpResponse(template.render(context,request))

# regisztrálás próbája
def tesztRegisztral(request):
    print("⚠️ teszt regisztráció / tesztRegisztral(request)")

    if request.method == "POST":
        # teszt regisztrálás létrehozása
        tesztRegisztraciosLap = Regisztralas(request.POST)

        # valudálás ellenőrzés
        if tesztRegisztraciosLap.is_valid():
            regisztraltFelhasznalo = tesztRegisztraciosLap.Mentes()

            #frissen regisztrál felhasználó regisztrálása
            login(request, regisztraltFelhasznalo)
            
            # mi ként szeretne majd regisztrálni? Munka adó vagy munka vállaló?
    else:
        tesztRegisztraciosLap = Regisztralas()
    
    # válasz
    template = loader.get_template("app/tesztRegisztral.html")
    context = {
        "cim": "⚠️ tesztRegisztrálás",
        "form": tesztRegisztraciosLap
    }
    return HttpResponse(template.render(context,request))

# regisztrálás munkavállalóként
def tesztRegisztralMunkaV(request):
    print("⚠️ test regisztáció munkavállalóként / tesztRegisztralMunkaV(request)")

    if request.method == "POST":
        tesztRegisztraciosLap = Regisztralas(request.POST)
        tesztMunkaVallalo_Kiegeszito = MunkaVallalo_Kiegeszito(request.POST)

        if tesztRegisztraciosLap.is_valid() and tesztMunkaVallalo_Kiegeszito.is_valid():
            regisztraltFelhasznalo = tesztRegisztraciosLap.Mentes()

            #frissen regisztrál felhasználó regisztrálása
            login(request, regisztraltFelhasznalo)
            munkaVallaoKieg = MunkaVallalo_Kiegeszito.Mentes(request.user.username, request.user.email)
            munkaVallaoKieg.save()
            
    else:
        tesztRegisztraciosLap = Regisztralas()
        tesztMunkaVallalo_Kiegeszito = MunkaVallalo_Kiegeszito()

        # if tesztRegisztraciosLap.is_valid() and tesztMunkaVallalo_Kiegeszito.is_valid():
        #     regisztraltFelhasznalo = tesztRegisztraciosLap.Mentes()

        #     #frissen regisztrál felhasználó regisztrálása
        #     login(request, regisztraltFelhasznalo)
        #     munkaVallaoKieg = MunkaVallalo_Kiegeszito.Mentes(request.user.username, request.user.email)

    template = loader.get_template("app/tesztRegisztral_es_Munkavallalo.html")
    context = {
        "cim": "⚠️ tesztRegisztrálá és munkavállaló",
        "form": tesztRegisztraciosLap,
        "form1": tesztMunkaVallalo_Kiegeszito
    }
    return HttpResponse(template.render(context,request))
