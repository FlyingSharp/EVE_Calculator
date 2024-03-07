from construction.ship.Ship import Ship
from extra_buffer.BufferData import BufferData


class ConventionalShip(Ship):

    def __init__(self, name: str) -> None:
        super().__init__(name)
        self._name_in_tree = "常规舰船"

    def get_extra_material_influence(self) -> float:
        return BufferData.conventional_ship_material_influence
