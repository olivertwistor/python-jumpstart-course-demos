"""
Main file for the Journal application.
"""

from journal import Journal
import ui


journal_file_name = "journal.txt"


def main():
    """
    Prints the app header, loads the journal and starts the program loop.
    """
    ui.print_header()
    journal = Journal.load(journal_file_name)
    run_program_loop(journal)


def run_program_loop(journal: Journal):
    """
    Runs the program loop: asking the user what do to, until the user chooses
    to exit the app.

    :param journal: The Journal object to work with
    :return:
    """
    cmd = "."
    while cmd and cmd != "x":
        cmd = ui.read_menu_input()

        if cmd == "l":
            ui.print_entries(journal.entries)
        elif cmd == "a":
            text = ui.read_add_entry_input()
            journal.add_entry(text)
        elif cmd == "x":
            journal.save(journal_file_name)
            exit(0)


if __name__ == '__main__':
    main()
