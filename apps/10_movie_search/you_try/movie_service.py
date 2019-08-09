"""
Service that works with the Open Movie Database API (TalkPython version).
"""

# API base URL.
import requests

from movie_model import Movie

base_url = "http://movie_service.talkpython.fm/api"


def search_titles(search_term: str) -> list:
    """
    Searches the API for movies that match the search term.

    :param search_term: Case insensitive word or phrase to search for.

    :return: A list of Movie tuples, with all the movies that match the search
             criteria.

    :raises HTTPError: If there was some error when using the API.
    :raises ValueError: If search term is None or empty; or if the API response
                        had malformed JSON.
    """

    # First check that we have a non-empty search term.
    if not search_term or not search_term.strip():
        raise ValueError()

    # Create the full API endpoint.
    api_endpoint = base_url + "/search/{}".format(search_term)

    # Get the response from the REST call and turn it into JSON. We are only
    # interested in the "hits" part of the response.
    response = requests.get(api_endpoint)
    response.raise_for_status()
    json = response.json()
    movie_list = json.get("hits")

    # Turn the JSON response into a list of Movie tuples.
    movies = [
        Movie(**ml)
        for ml in movie_list
    ]

    return movies
