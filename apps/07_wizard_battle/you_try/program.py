"""
Main program file for this application.
"""
from game import Game
import wizard_ui as ui


def main():
    """
    Prints the app header and starts the game.
    """
    ui.print_header()
    game = Game()
    game.start()
    game.run()


if __name__ == '__main__':
    main()
