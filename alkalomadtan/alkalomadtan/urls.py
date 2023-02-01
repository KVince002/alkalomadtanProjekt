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
from django.urls import path, include

urlpatterns = [
    # Admin oldal
    path('admin/', admin.site.urls),
    path("", views.Homepage, name="Kezdőlap"),
    path("rolunk/", views.Rolunk, name="Rolunk"),
    path("munkak/", views.Allasok, name="Munak"),
    path("blog/", views.Blog, name="Blog"),

    # teszt oldalak
    path("tesztRegisztral/", views.tesztRegisztral, name="tesztRegisztral"),
    path("tesztRegisztralMunkavallalo/", views.tesztRegisztralMunkaV, name="tesztRegisztralMunkaV")
]
