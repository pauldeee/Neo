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
    path('buy', views.buy, name="buy"),
    path('sell', views.sell, name="sell"),
    path('start_bot', views.start_bot, name="start_bot"),
    path('stop_bot', views.stop_bot, name="stop_bot"),
    path('backtest', views.backtest, name="backtest"),
    path('<str:tid>', views.ticker, name="ticker"),

]
