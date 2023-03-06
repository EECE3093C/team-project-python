from django.shortcuts import render
from django.template import loader
from .models import Building

# Create your views here.


def home(request):
    context = {}
    return render(request, 'pathfinder/UCRouteMainPage.html', context)


def routefinder(request):
    buildings = Building.objects.all()
    context = {'buildings': buildings}
    return render(request, 'pathfinder/FindRouteApp.html', context)


def obstruction(request):
    context = {}
    return render(request, 'pathfinder/obstruction.html', context)


def obstruction_sent(request):
    context = {}
    return render(request, 'pathfinder/obstruction_sent.html', context)


def result(request):
    context = {}
    return render(request, 'pathfinder/result.html', context)
