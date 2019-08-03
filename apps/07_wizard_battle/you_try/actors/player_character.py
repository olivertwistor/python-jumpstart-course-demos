import random

from actors.actor import Actor


class PlayerCharacter(Actor):

    def __init__(self, name: str, level: int):
        super().__init__(name, level)
        self.attack_mod = 1.0

    def attack(self) -> int:
        """
        Performs a standard attack. The formula for calculating attack strength
        is as follows: actor level * attack modifier * random(1-12).

        :rtype: int
        :return: The attack strength.
        """

        attack_strength = self.level * self.attack_mod * random.randint(1, 12)
        attack_strength = int(attack_strength)

        return attack_strength

    @staticmethod
    def select_action() -> str:
        """
        Presents the player with a choice of actions to take and returns what
        the player has chosen.

        The user input is stripped from any whitespace and the string is made
        lowercase.

        :rtype: str
        :return: The player choice, stripped from whitespace and is made
                 lowercase.
        """
        user_input = input(
            "Do you want to [a]ttack, [r]un away, [l]ook around or [q]uit? "
        )
        user_input = user_input.strip().lower()

        return user_input
