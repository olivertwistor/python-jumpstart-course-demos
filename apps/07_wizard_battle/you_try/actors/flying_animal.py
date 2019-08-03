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
        self.defense_mod *= 2
