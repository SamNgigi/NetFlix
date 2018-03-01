import requests
from django.conf import settings
# api_key and base_url
api_key = settings.MOVIE_DATABASE_API_KEY
base_url = settings.MOVIE_DATABASE_URL


def get_movies():

    get_movies_url = base_url.format(api_key)
    response = requests.get(get_movies_url)
    movie_data = response.json()

    return movie_data
