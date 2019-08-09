"""
Main program file for this application.
"""
import collections
import os


# Named tuple representing a matched text.
MatchedText = collections.namedtuple("MatchedText", "file, line_number, text")


def main():
    """
    Input, processing and output loop.
    """

    print_header()

    root_folder = None
    try:
        root_folder = ask_user_for_root_folder()
    except NotADirectoryError as e:
        print(e.strerror)

    search_text = ask_user_for_search_text()
    matches = search_folders(root_folder, search_text)
    for match in matches:
        pretty_print(match)


def print_header():
    """
    Prints out a header for this app to stdout.
    """
    print("-----------------")
    print("FILE SEARCHER APP")
    print("-----------------")
    print()


def ask_user_for_root_folder() -> str:
    """
    Asks the user from which folder to start the search.

    :rtype str:
    :return: The absolute path to the folder.

    :raises
    """

    user_input = input("Specify a folder from which to start the search: ")
    full_path = os.path.abspath(user_input)
    if not os.path.isdir(full_path):
        raise NotADirectoryError("The specified path is not a folder.")

    return full_path


def ask_user_for_search_text() -> str:
    """
    Asks the user for which string to search.

    :rtype: str
    :return: The search string in lowercase, stripped from all leading and
             trailing whitespace.
    """

    user_input = input(
        "Specify a search string for which to search (only single phrase): "
    )
    user_input = user_input.strip()
    user_input = user_input.lower()

    return user_input


def search_folders(folder: str, text: str):
    """
    Recursively searches a folder for occurrences of text inside files. Each
    occurrence knows from which file it came, which line number and the line
    itself.

    :param folder: Absolute path to the folder in which to search.
    :param text: The text for which to search.
    """

    # List all files and subfolders within the supplied folder.
    files = os.listdir(folder)

    for file in files:

        # Make it an absolute path since os.listdir only returns relative paths.
        file_abspath = os.path.join(folder, file)

        # If the "file" is a folder, go into that folder.
        if os.path.isdir(file_abspath):
            yield from search_folders(file_abspath, text)
        else:
            yield from search_in_file(file_abspath, text)


def search_in_file(file: str, text: str):
    """
    Searches a file for all occurrences of a text. Each occurrence knows from
    which file it came, which line number and the line itself.

    :param file: Absolute path to the file in which to search.
    :param text: The text for which to search
    """

    try:
        with (open(file, "r", encoding="utf-8")) as fin:

            line_number = 0

            # Go line by line. If we find a matches, we yield them to the caller
            # as a named tuple.
            for line in fin:
                line_number += 1
                if line.lower().find(text) >= 0:
                    match = MatchedText(
                        file=file, line_number=line_number, text=line.strip()
                    )
                    yield match
    except UnicodeDecodeError:
        print("Found binary file {}. Skipping...".format(file))
        print()


def pretty_print(matched_text: MatchedText):
    """
    Prints out a MatchedText tuple to stdout, in a pretty format.

    :param matched_text: The MatchedText to print.
    """

    print("Match found")
    print("-----------")
    print("File:        {}".format(matched_text.file))
    print("Line number: {:n}".format(matched_text.line_number))
    print("Text:        {}".format(matched_text.text))
    print()


if __name__ == '__main__':
    main()
