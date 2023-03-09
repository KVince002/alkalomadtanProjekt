from django import forms
from django.forms import ModelForm
from app.models import *

# autentikáló mudolok
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.forms.fields import EmailField

# kollektív fiók regisztrálás
class Regisztralas(forms.Form):   
    felhasznaloNev = forms.CharField(label="Felhasználónév", min_length=3, max_length=150)
    eloNev = forms.CharField(label="Előnév", max_length=150)
    utoNev = forms.CharField(label="Utónév", max_length=150)
    email = forms.EmailField(label="Email cím", widget=forms.EmailInput)
    jelszo1 = forms.CharField(label="Jelszava", widget=forms.PasswordInput)
    jelszo2 = forms.CharField(label="Jelszava még egyszer", widget=forms.PasswordInput)

    # ezekkel a függvényekkel olvassuk és ellenőrizzük az adatokat amiket a From filed-ekből szerzünk meg
    def clean_felhasznalo(self):
        felhasznaloNev = self.cleaned_data['felhasznaloNev'].lower()
        keres = User.objects.filter(username=felhasznaloNev)
        if keres.count():
            raise ValidationError("Ez a felhasználónév már létezik!")
        return felhasznaloNev

    def clean_email(self):
        email = self.cleaned_data["email"].lower()
        keres = User.objects.filter(email=email)
        if keres.count():
            raise ValidationError("Ez az email címmel már regisztráltak!")
        return email

    def clean_eloNev(self):
        eloNev = self.cleaned_data["eloNev"].lower()
        return eloNev

    def clean_utoNev(self):
        utoNev = self.cleaned_data["utoNev"].lower()
        return utoNev
    # ezzel lehet ellenőrizni hogy a két jelszó mező egyezik-e

    def clean_jelszomegint(self):
        jelszo1 = self.cleaned_data["jelszo1"]
        jelszo2 = self.cleaned_data["jelszo2"]
        if jelszo1 != jelszo2:
            raise ValidationError("A jelszavak nem egyeznek!")
        # if jelszo1 != "" or jelszo2 != "":
        #     raise ValidationError("Biztos hogy kitöltötte a két jelszőmezőt?")
        return jelszo2

    def Mentes(self):
        felhasznalo = User.objects.create_user(
            username = self.clean_felhasznalo(),
            email = self.clean_email(),
            password = self.clean_jelszomegint(),
        )
        felhasznalo.first_name = self.clean_eloNev()
        felhasznalo.last_name = self.clean_utoNev()
        felhasznalo.save()
        
        return felhasznalo

class JelentkezesFormModel(ModelForm):
    class Meta:
        model = Jelentkezes
        fields = "__all__"
        exclude =["munkaVallalo","ido", "felhId", "munka"]
    
    berigeny = forms.IntegerField(label="Bérigényed")
    bemutatkozas = forms.Textarea()
    melleklet = forms.FileField(label="Melléklet", required=True)

    def save(self,commit=True):
        instance = super(JelentkezesFormModel,self).save(commit=False)
        fajl = self["melleklet"].value()
        print(fajl)
        if commit:
            instance.save()
        return instance

# nagyon bugyuta form
class BejelentkezesForm(forms.Form):
    email = forms.EmailField(label="Email címe", widget=forms.EmailInput)
    jelszo = forms.CharField(label="Jelszava", widget=forms.PasswordInput)

class MunkaFrom(ModelForm):
    class Meta:
        model = Munka
        fields = "__all__"
        exclude = ["publikalo", "katt"]

    nev = forms.CharField(label="Munka neve", max_length=250)
    leiras = forms.TextInput()
    helye = forms.CharField(label="Munkka végzésének a helye:", max_length=150)
    berMin = forms.IntegerField(label="Minimum bér")
    berMax = forms.IntegerField(label="Maximum bér")
    munkaKezd = forms.DateField(label="Munka kezdésének az időpontja")