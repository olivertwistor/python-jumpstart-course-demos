from actors.animal import Animal
from actors.dragon import Dragon
from actors.flying_animal import FlyingAnimal
from actors.small_animal import SmallAnimal
from actors.wizard import Wizard


class Game:
    """
    This class models a game session. It keeps track of the player character,
    the active monsters, win/lose conditions and everything else needed for
    one game session.
    """

    def __init__(self):
        """
        Creates a player character in the form of a wizard and a number of
        enemies.
        """

        self.player_character = Wizard("Gandolf", 75)
        self.enemies = [
            SmallAnimal("Toad", 1),
            FlyingAnimal("Bat", 3),
            Animal("Tiger", 12),
            Dragon("Fire Dragon", 50),
            Wizard("Saruman", 300)
        ]

    def start(self):
        """
        Prints an opening statement of the game to stdout.
        """
        print("You are {} and you wake up in the middle of a forest. To be "
              "able to get home, you need to defeat all the enemies standing "
              "in your way.".format(self.player_character))
        print()

    def run(self):
        """
        The main game loop. Asks the user what do to, performs that action and
        loops around until either the win condition or the lose condition has
        been met.
        """

        win_condition = False
        lose_condition = False

        while not (win_condition or lose_condition):

            action = self.player_character.select_action()
            if (action)

    def end(self):
        raise NotImplementedError
