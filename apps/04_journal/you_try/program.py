"""
Main file for the Journal application.
"""

from journal import Journal
import ui


def main():
    """
    Prints the app header, loads the journal and starts the program loop.
    """
    ui.print_header()
    journal = Journal.load()
    run_program_loop()


def run_program_loop():
    pass


if __name__ == '__main__':
    main()
