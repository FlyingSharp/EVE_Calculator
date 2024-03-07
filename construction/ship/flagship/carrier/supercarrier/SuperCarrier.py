from construction.ship.flagship.carrier.Carrier import Carrier


class SuperCarrier(Carrier):

    def __init__(self, name: str) -> None:
        super().__init__(name)
        self._name_in_tree = "超级航母"
        self._manufacturing_costs = 5000000000

