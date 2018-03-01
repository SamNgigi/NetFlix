from django.shortcuts import render
# import requests
from .fetch import get_movies
# Create your views here.


def index(request):
    # test = 'Working'
    popular = get_movies('popular')
    return render(request, 'index.html', {"popular": popular})
