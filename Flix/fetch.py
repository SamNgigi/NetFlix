import requests
from django.conf import settings
# api_key and baseurl
api_key = settings.MOVIE_DATABASE_API_KEY
base_url = settings.MOVIE_DATABASE_URL


def get_movies():

    get_movies_url = base_url.format(api_key)
    response = requests.get(get_movies_url)
    movie_data = response.json()
    videos = movie_data['videos']
    trailer = videos['results']
    youtube_trailer = trailer[0]['key']
    print(youtube_trailer)

    content = {
        'title': movie_data['title'],
        'poster': movie_data['poster_path'],
        'trailer': youtube_trailer
    }
    # print(content)
    return content
