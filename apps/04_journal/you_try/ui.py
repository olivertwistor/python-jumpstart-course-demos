"""
This file contains functions that manages the UI.
"""


def print_header():
    """
    Prints the program header to stdout.

    :since: 0.1.0
    """
    print("--------------------")
    print("PERSONAL JOURNAL APP")
    print("--------------------")
    print()


def read_menu_input() -> str:
    """
    Prints the available menu options. Reads user input, strips all whitespace
    and makes it lowercase.

    :return str: User input, stripped of whitespace and made to lowercase.
    """
    raw_input = input("What do you want to do ([L]ist, [A]dd, E[x]it)? ")
    stripped_input = raw_input.strip()
    lowercase = stripped_input.lower()

    return lowercase


def read_add_entry_input() -> str:
    """
    Lets the user write a journal entry. All this function does is appending a
    line feed to user input before returning.

    :return: The user input appended with a line feed.
    """
    text = input("Journal entry: ")
    text_with_line_feed = text + "\n"   # My research tells me that \n works on
                                        # Windows, too.

    return text_with_line_feed


def print_entries(entries: list, reverse_order=True):
    """
    Prints out the entries to stdout. If the list is empty, the output states
    so.

    :param entries: List of journal entries
    :param reverse_order: Whether or not to reverse the list before printing it.
    """

    if entries:
        if reverse_order:
            for idx, entry in enumerate(reversed(entries)):
                entry = entry.strip()
                print("{}. {}".format(1 + idx, entry))
        else:
            for idx, entry in enumerate(entries):
                print("{}. {}".format(1 + idx, entry))
    else:
        print("The journal is empty.")
