from django.shortcuts import render
# import requests
from .fetch import get_movies
# Create your views here.


def index(request):
    test = 'Working'
    movie_data = get_movies()
    videos = movie_data['videos']
    trailer = videos['results']
    youtube_trailer = trailer[0]['key']
    print(youtube_trailer)

    content = {
        "test": test,
        'title': movie_data['title'],
        'poster': movie_data['poster_path'],
        'trailer': youtube_trailer
    }

    return render(request, 'index.html', content)
