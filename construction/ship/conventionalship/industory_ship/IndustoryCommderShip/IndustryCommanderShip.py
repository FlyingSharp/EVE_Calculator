from construction.ship.conventionalship.industory_ship.IndustryShip import IndustryShip


class IndustryCommanderShip(IndustryShip):

    def __init__(self, name: str) -> None:
        super().__init__(name)
        self._name_in_tree = "工业指挥舰"
        self._manufacturing_costs = 300000000
