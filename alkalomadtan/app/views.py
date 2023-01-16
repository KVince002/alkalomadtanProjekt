from django.shortcuts import render
from django.template import loader
from django.http import HttpRequest, HttpResponse
from app.forms import Regisztralas, MunkaVallalo_Kiegeszito
from django.contrib.auth import logout, authenticate, login

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

def tesztRegisztral(request):
    print("⚠️ teszt regisztráció / tesztRegisztral()")

    if request.method == "POST":
        # teszt regisztrálás létrehozása
        tesztRegisztraciosLap = Regisztralas(request.POST)

        # valudálás ellenőrzés
        if tesztRegisztraciosLap.is_valid():
            regisztraltFelhasznalo = tesztRegisztraciosLap.mentes()

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