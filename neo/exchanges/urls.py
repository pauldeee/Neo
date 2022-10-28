from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('add_api', views.add_api, name="add_api"),
]
