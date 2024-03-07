from construction.ship.flagship.Flagship import Flagship


class IndustryFlagShip(Flagship):

    def __init__(self, name: str) -> None:
        super().__init__(name)
        self._name_in_tree = "旗舰级工业舰"
        self._manufacturing_costs = 3500000000

