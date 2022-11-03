from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('account', views.account, name="account"),
    path('api', views.api, name="api"),
    path('history', views.history, name="history"),
    path('trading', views.trading, name="trading"),
    path('news', views.news, name="news"),
    path('reports', views.reports, name="reports"),
    path('search', views.search, name="search"),
    path('<str:tid>', views.ticker, name="ticker"),
]
