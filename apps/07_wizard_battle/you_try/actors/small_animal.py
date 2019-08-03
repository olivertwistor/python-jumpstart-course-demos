from actors.animal import Animal


class SmallAnimal(Animal):
    """
    A small animal is a special kind of animal, in that it only does half the
    attack damage it normally would if it was a normal-sized animal.
    """

    def __init__(self, name: str, level: int):
        """
        Creates a small animal with a name/identifier and a level. Sets the
        attack modifier to 0.5.

        :param name: Something that identifies this small animal to the player.
        :param level: Level of this small animal; must be greater than 0.

        :raises ValueError: If the supplied level isn't greater than 0.
        """

        super().__init__(name, level)
        self.attack_mod = 0.5
