from django.shortcuts import render
from django.template import loader
from .models import Building

# Create your views here.
from django.http import HttpResponse


def index(request):
    context = {}
    return render(request, 'pathfinder/UCRouteMainPage.html', context)


def routefinder(request):
    buildings = Building.objects.all()
    context = {'buildings': buildings}
    return render(request, 'pathfinder/FindRouteApp.html', context)


def result(request):
    context = {}
    return render(request, 'pathfinder/result.html', context)
