from django.shortcuts import render
import requests

# Create your views here.


def index(request):
    test = 'Working'
    response = requests.get(
        'http://api.themoviedb.org/3/movie/157336?api_key=5c680a4136f5ea00d164efb422804b99&append_to_response=videos')
    movie_data = response.json()
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
