from django.shortcuts import render
# import requests
from .fetch import get_movies
# Create your views here.


def index(request):
    # test = 'Working'
    content = get_movies()

    return render(request, 'index.html', content)
