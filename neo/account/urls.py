from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('account', views.account, name="account")
]
