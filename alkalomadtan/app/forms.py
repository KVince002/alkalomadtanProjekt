from django import forms
from django.forms import ModelForm
from app.models import MunkaAdo, MunkaVallalo, Munka, Jelentkezes

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

    def mentes(self, commit=True):
        felhasznalo = User.objects.create_user(
            username = self.clean_felhasznalo(),
            email = self.clean_email(),
            password = self.clean_jelszomegint(),
        )
        felhasznalo.first_name = self.clean_eloNev()
        felhasznalo.last_name = self.clean_utoNev()
        felhasznalo.save()
        
        return felhasznalo

# 🚫 befejeztetlen
class MunkaVallalo_Kiegeszito(forms.ModelForm):
    
    class Meta:
        model = MunkaVallalo
        fields = ("telefon", "email", "erdekelt")
    telefon = forms.CharField(label="Telefonszám", max_length=11, required=True)
