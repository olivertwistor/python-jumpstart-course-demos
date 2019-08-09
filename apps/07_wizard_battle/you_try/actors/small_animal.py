from actors.animal import Animal


class SmallAnimal(Animal):
    """
    A small animal is a special kind of animal, in that it only has half the
    defense modifier of what a normal-sized animal has.
    """

    def __init__(self, name: str, level: int):
        """
        Creates a small animal with a name/identifier and a level. Sets the
        defense modifier to half that of its superclass.

        :param name: Something that identifies this small animal to the player.
        :param level: Level of this small animal; must be greater than 0.

        :raises ValueError: If the supplied level isn't greater than 0.
        """

        super().__init__(name, level)
        self.defense_mod *= 0.5
