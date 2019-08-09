"""
UI for the movie search app.
"""


def print_header():
    """
    Prints app header to stdout.
    """
    print("----------------")
    print("MOVIE SEARCH APP")
    print("----------------")
    print()


def print_movie_info(movies: list):
    """
    Prints info about movies to stdout. The list is sorted by title in
    alphabetical order.

    :param movies: A list of Movie tuples that should be printed.
    """

    # Sort the list by title in alphabetical order.
    sorted_movies = sorted(movies, key=lambda m: m.title)

    # Print out movie info, one line per movie.
    for movie in sorted_movies:
        print("{1} ({2}, {3}) -- https://www.imdb.com/title/{0}".format(
            movie.imdb_code, movie.title, movie.director, movie.year))
