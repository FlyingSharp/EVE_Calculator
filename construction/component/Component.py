from construction.EnhancedItem import EnhancedItem
from extra_buffer.BufferData import BufferData


class Component(EnhancedItem):

    def __init__(self, name: str) -> None:
        super().__init__(name)
        self._manufacturing_costs = 150000000.0
        self._name_in_tree = "旗舰组件"

    def get_extra_material_influence(self) -> float:
        return BufferData.ship_component_material_influence
