from construction.ship.flagship.Flagship import Flagship


class Carrier(Flagship):

    def __init__(self, name: str) -> None:
        super().__init__(name)
        self._name_in_tree = "航空母舰"
        self._manufacturing_costs = 2000000000
