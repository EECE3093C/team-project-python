from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('findroute/', views.routefinder, name='routefinder'),
    path('obstruction/', views.obstruction, name='obstruction'),
    path('obstruction/sent/', views.obstruction_sent, name='obstruction_sent'),
    path('result/', views.result, name='result'),
    # path('<str:start>/<str:end>/result, views.result, name='result')
]

