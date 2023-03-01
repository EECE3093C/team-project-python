from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('findroute/', views.routefinder, name='routefinder'),
    path('result/', views.result, name='result'),
]
