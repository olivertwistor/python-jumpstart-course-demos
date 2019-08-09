import random


class Actor:
    """
    This class is the base class for all player characters, non-player
    characters and monsters in the game.
    """

    def __init__(self, name: str, level: int):
        """
        Creates an actor with a name/identifier and a level. Also adds a
        defense modifier initialized to 1.0.

        :param name: Something that identifies this actor to the player.
        :param level: Level of this actor; must be greater than 0.

        :raises ValueError: If the supplied level isn't greater than 0.
        """

        if level <= 0:
            raise ValueError("Level must be greater than 0.")

        self.name = name
        self.level = level
        self.defense_mod = 1.0

    def __str__(self):
        """
        Returns a string representation of this actor: the name and the level.

        :return: string
        """

        return "{} [{}]".format(self.name, self.level)

    def defend(self) -> int:
        """
        Performs a standard defensive maneuver. The formula for calculating
        defense strength is as follows: actor level * defense modifier *
        random(1-12).

        :rtype: int
        :return: The defense strength.
        """

        defense_strength = self.level * self.defense_mod * random.randint(1, 12)
        defense_strength = int(defense_strength)

        return defense_strength
