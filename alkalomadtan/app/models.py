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
    # munka napok kivéve, át dolgozás kell neki
    # munkanapok és óraszámok. Ez egy map/szótár-t fog majd tárolni. A szótár inex: napok; érték: óraköz
    # munkaNapok = models.TextField()

    def __str__(self):
        return f"Munka neve: {self.nev}, publikáló: {self.publikalo}, hely: {self.helye}"

# jelentkezés modell
def fajlNevGeneralo(self, fajlnev):
    url = "feltoltottDokumentumok/felh_%s/%s" % (self.felhId, fajlnev)
    return url
# rekreálás a megbeszéltek alapján
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
    # önéletrajz 
    felhId = models.CharField(max_length=10, null=False, default="")
    melleklet = models.FileField(null = False, upload_to=fajlNevGeneralo)

    def __str__(self):
        return f"{self.munka} - {self.ido}-kor jelentkezett: {self.munkaVallalo}"