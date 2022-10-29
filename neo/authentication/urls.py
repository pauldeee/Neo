from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('signup', views.signup, name="signup"),
    path('signin', views.signin, name="signin"),
    path('signout', views.signout, name="signout"),
    path('add_api', views.add_api, name="add_api"),
]
