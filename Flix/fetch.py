import requests
from django.conf import settings
from .models import Movie
# api_key and baseurl
api_key = settings.MOVIE_DATABASE_API_KEY
base_url = settings.MOVIE_DATABASE_URL


def get_movies(category):

    get_movies_url = base_url.format(category, api_key)
    response = requests.get(get_movies_url)
    get_movies_response = response.json()

    if get_movies_response['results']:
        movie_results_list = get_movies_response['results']
        movie_results = process_results(movie_results_list)

    # print(content)
    return movie_results


def process_results(movie_list):
    '''
    Function  that processes the movie result and transform
    them to a list of Objects
    Args:
        movie_list: A list of dictionaries that contain movie details
    Returns :
        movie_results: A list of movie objects
    '''
    movie_results = []
    # movie_dict = {}
    for movie_item in movie_list:
        id = movie_item.get('id')
        title = movie_item.get('original_title')
        overview = movie_item.get('overview')
        poster = movie_item.get('poster_path')
        vote_average = movie_item.get('vote_average')
        vote_count = movie_item.get('vote_count')

        if poster:
            movie_object = Movie(id, title, overview,
                                 poster, vote_average, vote_count)
            movie_results.append(movie_object)

    return movie_results
