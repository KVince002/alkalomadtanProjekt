from multiprocessing import context
from re import template
from django.shortcuts import render
from django.template import loader
from django.http import HttpRequest, HttpResponse

# Create your views here.
# kezdőlap
def homepage(request):
    print("Kezdőlap / homepage()")

    # Válaszadó
    template = loader.get_template("app/home.html")
    context = {
        "cim": "Kezdőlap"
        }
    return HttpResponse(template.render(context,request))

def munkak(request):
    print("Munka lista / munkak()")

    # Válaszadó
    