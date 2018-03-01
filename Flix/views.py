from django.shortcuts import render
# import requests
from .fetch import get_movies
# Create your views here.


def index(request):
    # test = 'Working'
    popular = get_movies('popular')
    upcoming = get_movies('upcoming')
    now_playing = get_movies('now_playing')

    content = {
        "popular": popular,
        "upcoming": upcoming,
        "now_playing": now_playing,
    }
    return render(request, 'index.html', content)
