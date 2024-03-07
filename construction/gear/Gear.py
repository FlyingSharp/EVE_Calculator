from construction.EnhancedItem import EnhancedItem
from extra_buffer.BufferData import BufferData


class Gear(EnhancedItem):

    def __init__(self, name: str) -> None:
        super().__init__(name)
        self._name_in_tree = "装备"

    def get_extra_material_influence(self) -> float:
        return BufferData.gear_material_influence
