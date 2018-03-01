from django.shortcuts import render
# import requests
from .fetch import get_movies
# Create your views here.


def index(request):
    test = 'Working'

    movie = get_movies()
    print(movie)
    return render(request, 'index.html', {"test": test})
