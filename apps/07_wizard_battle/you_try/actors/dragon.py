import random

from actors.flying_animal import FlyingAnimal


class Dragon(FlyingAnimal):
    """
    A dragon is a special kind of flying animal, in that because of it
    breathing fire, its attack modifier is increases, and because of its
    scales, its defense modifier is increased.
    """

    def __init__(self, name: str, level: int):
        """
        Creates a dragon with a name/identifier and a level. Adds a random d6
        roll to flying animals' usual attack modifier, and a random d4 roll to
        flying animals' usual defense modifier.

        :param name: Something that identifies this dragon to the player.
        :param level: Level of this dragon ; must be greater than 0.

        :raises ValueError: If the supplied level isn't greater than 0.
        """

        super().__init__(name, level)
        self.attack_mod += random.randint(1, 6)
        self.defense_mod += random.randint(1, 4)
