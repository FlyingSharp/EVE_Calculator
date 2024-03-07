from construction.ship.conventionalship.ConventionalShip import ConventionalShip


class IndustryShip(ConventionalShip):

    def __init__(self, name: str) -> None:
        super().__init__(name)
        self._name_in_tree = "工业舰"
