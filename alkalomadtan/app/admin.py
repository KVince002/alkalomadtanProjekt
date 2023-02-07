from django.contrib import admin
from app.models import *

# /admin oldal modell megtekintői
# munkaVallalo
# class MunkaVallaoAdmin(admin.ModelAdmin):
#     fields = ["bemutatkozas",
#               "telefon",
#               "email",
#               "eretkeles",
#               "erdekelt"]

# # munkaAdo
# class MunkaAdoAdmin(admin.ModelAdmin):
#     fields = ["nev",
#               "bemutatkozas",
#               "telefon",
#               "email",
#               "ertekeles"]

# munka
class MunkdaAdmin(admin.ModelAdmin):
    fields = ["nev",
              "leiras",
              "helye",
              "katt",
              "publikalo",
              "berMin",
              "berMax",
              "munkaKezd"]

# jelentkezes
class JelentkezesAdmin(admin.ModelAdmin):
    fields = ["munkaVallalo",
              "munka",
              "ido",
              "berigeny",
              "bemutatkozas",
              "melleklet"]
    
# modellek regisztrálása a az admin felületre
# admin.site.register(MunkaVallalo, MunkaVallaoAdmin)
# admin.site.register(MunkaAdo, MunkaAdoAdmin)
admin.site.register(Munka, MunkdaAdmin)
admin.site.register(Jelentkezes, JelentkezesAdmin)