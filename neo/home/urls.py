from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('home', views.home, name="home"),
    path('about', views.about, name='about'),
    path('faq', views.faq, name='faq'),
    path('howto', views.howto, name='howto'),
    # path('about', views.about, name='about'),
    # path('signup', views.signup, name="signup"),
    # path('signin', views.signin, name="signin"),
    # path('signout', views.signout, name="signout"),
]
