import random

from actors.actor import Actor
from actors.animal import Animal
from actors.dragon import Dragon
from actors.flying_animal import FlyingAnimal
from actors.player_character import PlayerCharacter
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
        Creates a player character and a number of enemies.
        """

        self.player_character = PlayerCharacter("Gandolf", 10)
        self.enemies = [
            SmallAnimal("Toad", 1),
            FlyingAnimal("Bat", 1),
            Animal("Tiger", 1),
            Dragon("Fire Dragon", 1),
            Wizard("Saruman", 1)
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
        loss_condition = False

        while not (win_condition or loss_condition):

            # First, check to see that there still are enemies alive. If not,
            # break into end mode.
            if not self.enemies:
                self.end(True, False)

            # Select a random enemy and present that enemy to the player.
            enemy = random.choice(self.enemies)
            print("{} is blocking your path.".format(enemy))

            # Get the player action.
            action = self.player_character.select_action()

            if action == "a":
                player_won = self.commence_battle(self.player_character, enemy)
                if player_won:
                    self.enemies.remove(enemy)
                else:
                    self.end(False, True)

            elif action == "r":
                print("You run away from this fight.")

            elif action == "l":
                print("You see the following enemies:")
                for this_enemy in self.enemies:
                    print("* {}".format(this_enemy))
                print()

            elif action == "q":
                self.end(win_condition, loss_condition)

            else:
                print("Unrecognized command.")

    @staticmethod
    def end(win_condition: bool, loss_condition: bool):

        if win_condition and not loss_condition:
            print("You have defeated all enemies and were able to return home "
                  "safely. Good job!")
        elif not win_condition and loss_condition:
            print("The enemies were too much for you to handle. Better luck "
                  "next time!")
        else:
            print("Something weird has happened. Either you both won and lost "
                  "at the same time, or you neither won nor lost. Either way, "
                  "it's not your fault. You should blame the developer.")

        exit(0)

    @staticmethod
    def commence_battle(attacker: PlayerCharacter, defender: Actor) -> bool:

        attacker_roll = attacker.attack()
        defender_roll = defender.defend()
        dealt_damage = attacker_roll - defender_roll

        print("{} attacks {}: {} against {}.".format(
            attacker, defender, attacker_roll, defender_roll))
        if dealt_damage >= 0:
            print("{} defeats {}.".format(attacker, defender))
            return True
        else:
            print("{} was defeated by {}.".format(attacker, defender))
            return False
