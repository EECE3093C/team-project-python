from django.shortcuts import render
from django.template import loader

# Create your views here.
from django.http import HttpResponse


def index(request):
    context = {}
    return render(request, 'pathfinder/UCRouteMainPage.html', context)


def routefinder(request):
    context = {}
    return render(request, 'pathfinder/FindRouteApp.html', context)
