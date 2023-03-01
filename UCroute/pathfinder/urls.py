from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('findroute/', views.routefinder, name='routefinder'),
    path('obstruction/', views.obstruction, name='obstruction'),
    path('result/', views.result, name='result'),
    # path('<str:start>/<str:end>/result, views.result, name='result')
]

