import imp
# from django import views
from app import views
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include

app_name = "app"

urlpatterns = [
    path("munkak/<int:munka_Id>", views.munkaMegtekinto, name="munka{munka_Id}")
]