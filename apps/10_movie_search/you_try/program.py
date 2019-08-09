"""
Main program file.
"""
from requests import HTTPError

import movie_service
import movie_ui as ui


def main():
    """
    Program flow.
    """
    ui.print_header()
    search_term = ""
    while search_term.lower() != "x":

        search_term = input(
            "Please enter a search term ('x' exits the app): ")

        try:
            search_results = movie_service.search_titles(search_term)

            print("Found {} movies matching the search term '{}'.".format(
                len(search_results), search_term))
            ui.print_movie_info(search_results)

        except ValueError:
            if not search_term:
                print("ERROR:  You can't search for an empty movie title.")
            else:
                print("ERROR:   The movie service returned malformed data.")
                exit(1)
        except HTTPError as e:
            print("ERROR:  A network error occurred. {}".format(e.response))
            exit(2)

        print()

    print("Good bye!")
    exit(0)


if __name__ == '__main__':
    main()
