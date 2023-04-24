"""alkalomadtan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import imp
# from django import views
from app import views
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.shortcuts import redirect

from rest_framework import routers


urlpatterns = [
    # Admin oldal
    path('admin/', admin.site.urls),

    # Főbb oldalak
    path("", views.Homepage, name="Kezdolap"),
    path("rolunk/", views.Rolunk, name="Rolunk"),
    path("munkak/", views.Allasok, name="Munkak"),
    path("munka_bemutato/",views.AllasokBemutato,name="MunkaBemutato"),
    path("kapcsolat/", views.Kapcsolat, name="Kapcsolat"),
    # ez az utvonal kifejezetten egy munkaára utal
    path("munkak/<int:munka_Id>", views.MunkaMegtekinto, name="MunkaReszlet"),

    # Oldalak Profilhoz
    path("profil/", views.Profil, name="Profil"),
    path("profil/meglevoMunka/", views.Profil_MeglevoMunka, name="ProfilMeglevoMunka"),
    path("profil/uj_munka/", views.Profil_UjMunka, name="ProfilUjMunka"),
    # jelentkezők az adott munkára link és letöltés
    path("profil/jelentkezok/<int:munka_Id>", views.Profil_JelentkezoMegtekinto, name="Jelentkezo_Per_Munka"),
    path("profil/jelentkezok/letoltes/<int:jelentkezes_id>", views.Profil_JelentkezoDokumentLetolto, name="Jelentkezo_munka_jelentkezo"),
    # munkák amire jelentkeztél
    path("profil/jelentkezesek/", views.Profil_Jelentkezesek, name="ProfilJelentkezesek"),
    # a kijelentkező link
    path("kijelentkezes/", views.KijelentkezKerelem, name="KijelentkezKerelem"),
    # az új regizstráló oldal
    path("regisztral/", views.Regisztral, name="Regisztral"), # type: ignore
    # Profil adatainak frissítése (rest)
    path("profil/modosit/<int:primaryKey>/", views.ProfilRestView.as_view(), name="ProfilModosit"),

    # django auth oldalak
    # Ezek a Django-ba beleépített oldalak "sablonok", ezek felül lehet írni, de csak óvatosan!
    # ez a django bejelentkezés kezelője
    path("bejelentkezes/", auth_views.LoginView.as_view(template_name="app/auth/login_auth.html", redirect_authenticated_user=True), name="bejelentkezes_auth"),
    # az a django jelszó helyre állító oldala (természetesen a profilokhoz!)
    path("jelszohelyre/", auth_views.PasswordResetView.as_view(
        template_name="app/auth/jelszoHelyre_auth.html"), name="jelszoHelyre_auth"),
    # ez a django jelszó változtatója
    path("jelszovalt/", auth_views.PasswordChangeView.as_view(
        template_name="app/auth/jelszoValt_auth.html"), name="jelszoValt_auth"),

    # teszt oldalak
    path("tesztRegisztral/", views.tesztRegisztral, name="tesztRegisztral"),
    path("tesztFeltolt/", views.tesztFileFel, name="tesztFileFel"),
    path("tesztBejelentkezes/", views.tesztBejelentkez, name="tesztBejelentkezes")
]
