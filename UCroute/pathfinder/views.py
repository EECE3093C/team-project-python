from django.shortcuts import render
from django.template import loader

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the pathfinder index.")


def routefinder(request):
    context = {}
    return render(request, 'pathfinder/findroute.html', context)
