from construction.ship.flagship.carrier.Carrier import Carrier

class MaintenanceSupportCarrier(Carrier):
    def __init__(self, name):
        super().__init__(name)
        self._name_in_tree = "战力辅助舰"
