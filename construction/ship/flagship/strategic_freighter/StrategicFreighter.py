from construction.ship.flagship.Flagship import Flagship


class StrategicFreighter(Flagship):

    def __init__(self, name: str) -> None:
        super().__init__(name)
        self._name_in_tree = "战略货舰"
        self._manufacturing_costs = 3500000000

