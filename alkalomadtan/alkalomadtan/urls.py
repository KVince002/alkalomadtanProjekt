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

urlpatterns = [
    # Admin oldal
    path('admin/', admin.site.urls),

    # Főbb oldalak
    path("", views.Homepage, name="Kezdőlap"),
    path("rolunk/", views.Rolunk, name="Rolunk"),
    path("munkak/", views.Allasok, name="Munak"),
    path("blog/", views.Blog, name="Blog"),
    path("profil/", views.Profil, name="Profil"),
    path("profil/ujmunka/", views.Profil_UjMunka, name="ProfilUjMunka"),
    #path("profil/jelentkezesek/"),

    # auth oldalak
    path("bejelentkezes/", auth_views.LoginView.as_view(template_name="app/auth/bejelentkezes_auth.html"), name="bejelentkezes_auth"),
    path("jelszohelyre/", auth_views.PasswordResetView.as_view(template_name="app/auth/jelszoHelyre_auth.html"), name="jelszoHelyre_auth"),
    path("jelszovalt/", auth_views.PasswordChangeView.as_view(template_name="app/auth/jelszoValt_auth.html"), name="jelszoValt_auth"),

    # teszt oldalak
    path("tesztRegisztral/", views.tesztRegisztral, name="tesztRegisztral"),
    path("tesztFeltolt/", views.tesztFileFel, name="tesztFileFel"),
    path("tesztBejelentkezes/", views.tesztBejelentkez, name="tesztBejelentkezes")
]
