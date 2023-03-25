from django import forms
from django.forms import ModelForm
from app.models import *

# autentikáló mudolok
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.forms.fields import EmailField

# kollektív fiók regisztrálás
class Regisztralas(UserCreationForm):
    # komment tisztítás
    first_name = forms.CharField(label="Előnév", max_length=150, required=True)
    last_name = forms.CharField(label="Utónév", max_length=150, required=True)

    class Meta:
        model = UserCreationForm.Meta.model
        # Mivel a UserCreationForm egy már meglévő osztály, de mi szeretnénk hoztáadni egy pár új mezőt. A user tábla már tartalmazza ezt a két mezőt csak alapértelmezetten nem tartalmazza az űrlap.
        fields = UserCreationForm.Meta.fields + ("first_name", "last_name") # type: ignore

    # ezekkel a függvényekkel olvassuk és ellenőrizzük az adatokat amiket a From filed-ekből szerzünk meg
    def clean_eloNev(self):
        eloNev = self.cleaned_data["eloNev"].lower()
        return eloNev

    def clean_utoNev(self):
        utoNev = self.cleaned_data["utoNev"].lower()
        return utoNev

class JelentkezesFormModel(ModelForm):
    class Meta:
        model = Jelentkezes
        fields = "__all__"
        exclude =["munkaVallalo","ido", "felhId", "munka"]
        labels = {
            "berigeny": "Bérigénye",
            "bemutatkozas": "Bemutatkozás",
            "melleklet": "Melléklet"
        }
    
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
        # melyik táblaát használja
        model = Munka
        # mely mezőkkel dolgozzon
        fields = "__all__"
        # mely menzőkkel NE dolgozzon
        exclude = ["publikalo", "katt"]

    nev = forms.CharField(label="Munka neve", max_length=250)
    leiras = forms.TextInput()
    helye = forms.CharField(label="Munkka végzésének a helye:", max_length=150)
    berMin = forms.IntegerField(label="Minimum bér")
    berMax = forms.IntegerField(label="Maximum bér")
    munkaKezd = forms.DateField(label="Munka kezdésének az időpontja")