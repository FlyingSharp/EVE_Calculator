from construction.EnhancedItem import EnhancedItem
from extra_buffer.BufferData import BufferData


class FlagShipGear(EnhancedItem):

    def __init__(self, name: str) -> None:
        super().__init__(name)
        self._manufacturing_costs = 0
        self._name_in_tree = "旗舰装备"

    def get_extra_material_influence(self) -> float:
        return BufferData.flag_ship_gear_material_influence
