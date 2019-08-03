import random


class Actor:
    """
    This class is the base class for all player characters, non-player
    characters and monsters in the game.
    """

    def __init__(self, name: str, level: int):
        """
        Creates an actor with a name/identifier and a level. Also adds an
        attack modifier property initialized to 1.0.

        :param name: Something that identifies this actor to the player.
        :param level: Level of this actor; must be greater than 0.

        :raises ValueError: If the supplied level isn't greater than 0.
        """

        if level <= 0:
            raise ValueError("Level must be greater than 0.")

        self.name = name
        self.level = level
        self.attack_mod = 1.0

    def __str__(self):
        """
        Returns a string representation of this actor: the name and the level.

        :return: string
        """

        return "{} (level {})".format(self.name, self.level)

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
