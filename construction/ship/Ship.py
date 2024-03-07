from construction.EnhancedItem import EnhancedItem
from extra_buffer.BufferData import BufferData


class Ship(EnhancedItem):

    def __init__(self, name: str) -> None:
        super().__init__(name)
        self._name_in_tree = "舰船"

    def get_extra_material_influence(self) -> float:
        return BufferData.flag_ship_material_influence
