from django.db import models
from django.conf import settings
from django.forms import CharField
# Django user modell importálása
import django.contrib.auth.models

# Create your models here
# munkavállalók
class MunkaVallalo(models.Model):
    # a becenév jó ötlet lett volna elsőre, ez feing key a user modelből
    azon = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # telefonszám
    telefon = models.CharField(max_length=11, null=False)
    # email
    email = models.EmailField(null=False)
    # értékelés a szám csillagokat jelöl
    eretkeles = models.FloatField(default=0)
    # érdekeltségi körök, ezt majd kömbként kell majd visszadnia
    erdekelt = models.CharField(max_length=255)

# # munka adó
class MunkaAdo(models.Model):
    # azonosítom a USER tábláből
    azon = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # telefonszám
    telefon = models.CharField(max_length=11, null=False)
    # email 
    email = models.EmailField(null=False)
    # értékelés a szám csillagokat jelöl
    ertekeles =models.FloatField(default=0)

# # munka
class Munka(models.Model):
    # munka neve
    nev = models.CharField(max_length=255, null=False)
    # munka leírása
    leiras = models.TextField(default="", null=False)
    # munka értéelése
    ertekeles = models.FloatField(default=0)
    # munka helye
    helye = models.CharField(default="", max_length=255)
    # kattintas
    katt = models.IntegerField(default=0)
    # publikalo
    publikalo = models.ForeignKey(MunkaAdo, on_delete=models.CASCADE)
    # bérsáv min (ez kötelező)
    berMin = models.IntegerField(null=False)
    # bársáv maximum 
    berMax = models.IntegerField(null=True)
    # mikor fog amjd a munka kezdődni
    munkaKezd = models.DateTimeField()
    # munkanapok és óraszámok. Ez egy map/szótár-t fog majd tárolni. A szótár inex: napok; érték: óraköz
    munkaNapok = models.TextField()


class Jelentkezes(models.Model):
    # munkáltaó
    munkaltato = models.ForeignKey(MunkaAdo, on_delete=models.CASCADE)
    # mukavállaló
    munkaVallalo = models.ForeignKey(MunkaVallalo, on_delete=models.CASCADE)
    # jelentkezés időpontja
    ido = models.DateTimeField(null=False)
    # berigeny
    berigeny = models.IntegerField(null=True)

