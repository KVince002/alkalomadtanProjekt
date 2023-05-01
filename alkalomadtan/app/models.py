from django.db import models
from django.conf import settings
from django.forms import CharField
# Django user modell importálása
import django.contrib.auth.models
# ido
from time import timezone
from datetime import datetime
import os

# # munka
class Munka(models.Model):
    class Meta:
        # rendezés kattintások szerint csökkenő sorba
        ordering = ["-katt"]
    
    # munka neve
    nev = models.CharField(max_length=255, null=False)
    # munka leírása
    leiras = models.TextField(default="", null=False)
    # munka helye
    helye = models.CharField(default="", max_length=255)
    # kattintas
    katt = models.IntegerField(default=0)
    # publikalo
    publikalo = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # bérsáv min (ez kötelező)
    berMin = models.IntegerField(null=False)
    # bársáv maximum 
    berMax = models.IntegerField(null=True)
    # mikor fog amjd a munka kezdődni
    munkaKezd = models.DateTimeField()

    def __str__(self):
        return f"Azon:{self.id}, Munka neve: {self.nev}, publikáló: {self.publikalo}"

# jelentkezés modell
def KonyvtarKezeles(instance, fajlNev):
    print(type(instance))
    # split() után tömböt kapunk
    fajlNev_Nyers = fajlNev.split(".")
    # eltároljuk a kiterjesztést
    fajlNev_Kiterjesztes = fajlNev_Nyers[len(fajlNev_Nyers)-1]
    # eltároljuk a fájl tényleges nevét
    fajlNev_Elnevez = fajlNev.strip("." + fajlNev_Kiterjesztes)

    # összerakás a kiegészítőkkel
    fajlNev_Finom = fajlNev_Elnevez + "-{0}_{1}".format(instance.munkaVallalo.first_name, instance.munkaVallalo.last_name)+ f"({instance.munkaVallalo.id})." + fajlNev_Kiterjesztes
    print(f"Finom fájlnév: {fajlNev_Finom}")
    return "feltoltottDokumentumok/munka_{0}/{1}".format(instance.munka.id,fajlNev_Finom)

class Jelentkezes(models.Model):
    # mukavállaló
    munkaVallalo = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # munka
    munka = models.ForeignKey(Munka, on_delete=models.CASCADE, default=0)
    # jelentkezés időpontja
    ido = models.DateTimeField(null=False, default=django.utils.timezone.now)
    # berigeny
    berigeny = models.IntegerField(null=True, default=0)
    # bemutatkozás
    bemutatkozas = models.TextField(null=True, default="A jelentkező nem írt leírást.")
    # önéletrajz mentése
    felhId = models.CharField(max_length=10, null=False, default="")
    melleklet = models.FileField(null = False, upload_to=KonyvtarKezeles, max_length=255)

    def __str__(self):
        return f"{self.munka} - {self.ido}-kor jelentkezett: {self.munkaVallalo}"

# django rest bemutato
# class Snippet(models.Model):
#     created = models.DateTimeField(auto_now_add=True)
#     title = models.CharField(max_length=100, blank=True, default='')
#     code = models.TextField()
#     linenos = models.BooleanField(default=False)
#     # mivel nincs meg a pygments csomag azért szerintme nem kell
#     # language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
#     # style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)
#     class Meta:
#         ordering = ['created']