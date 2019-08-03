from actors.actor import Actor


class Wizard(Actor):
    """
    A wizard is a humanoid actor with the ability to cast spells.
    """

    def __init__(self, name: str, level: int):
        """"
        Creates an actor with a name and a level. Also adds two spells: Fire
        and Heal.

        :param name: The name of this wizard.
        :param level: This wizard's level; must be greater than 0.

        :raises ValueError: If the supplied level isn't greater than 0.
        """

        super().__init__(name, level)
        self.spells = ["Fire", "Heal"]

    def attack(self):
        super().attack()
        raise NotImplementedError
