import random

from actors.animal import Animal


class FlyingAnimal(Animal):
    """
    A flying animal is a special kind of animal, in that because of its flying
    ability, it's twice as hard to hit.
    """

    def __init__(self, name: str, level: int):
        """
        Creates a flying animal with a name/identifier and a level. Sets the
        defense modifier to 2.

        :param name: Something that identifies this flying animal to the player.
        :param level: Level of this flying animal; must be greater than 0.

        :raises ValueError: If the supplied level isn't greater than 0.
        """

        super().__init__(name, level)
        self.defense_mod = 2

    def defend(self) -> int:
        """
        Performs a standard defensive maneuver. The formula for calculating
        defense strength is as follows: actor level * defense modifier *
        random(1-12).

        :return: The defense strength.
        """

        defense_strength = self.level * self.defense_mod * random.randint(1, 12)

        return defense_strength
