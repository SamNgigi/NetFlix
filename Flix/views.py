from django.shortcuts import render
import requests

# Create your views here.


def index(request):
    test = 'Working'
    response = requests.get(
        'https://api.themoviedb.org/3/movie/550?api_key=5c680a4136f5ea00d164efb422804b99')
    movie_data = response.json()
    content = {
        "test": test,
        'title': movie_data['title'],
        'poster': movie_data['poster_path'],
    }
    return render(request, 'index.html', content)
