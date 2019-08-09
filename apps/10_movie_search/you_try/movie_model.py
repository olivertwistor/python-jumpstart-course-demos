"""
Contains the model of a Movie.
"""
import collections


Movie = collections.namedtuple(
    "Movie", "imdb_code, title, director, keywords, duration, genres, rating, "
             "year, imdb_score")
