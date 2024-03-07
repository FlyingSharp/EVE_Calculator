from construction.ship.Ship import Ship
from extra_buffer.BufferData import BufferData


class Flagship(Ship):

    def __init__(self, name: str) -> None:
        super().__init__(name)
        self._name_in_tree = "旗舰"

    def get_extra_material_influence(self) -> float:
        return BufferData.flag_ship_gear_material_influence
