import Item
import consume.component.ComponentConsume as cmpcs
from typing import List, Tuple, Dict

class Component(Item):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def set_price(self, price) -> None:
        super().set_price(price)

    def get_pirce(self) -> float:
        super().get_pirce()

    def get_build_accessabled(self) -> bool:
        super().get_build_accessabled()

    def set_name(self, name) -> None:
        super().set_name(name)
    
    def get_name(self):
        super().get_name()

class BasicComponent(Component):
    _material_dict = None

    def __init__(self, name: str) -> None:
        super().__init__(name)
        
        if not self._material_dict:
            consume = cmpcs.ComponentConsume()
            self._material_dict = consume.parsing()
    
    def get_material_dict(self):
        return self._material_dict
    
    def set_price(self, price) -> None:
        super().set_price(price)

    def get_pirce(self) -> float:
        super().get_pirce()

    def get_build_accessabled(self) -> bool:
        super().get_build_accessabled()

    def set_name(self, name) -> None:
        super().set_name(name)
    
    def get_name(self):
        super().get_name()


class AdvancedComponent(Component):
    "超级旗舰专用组件"
    def __init__(self, name) -> None:
        super().__init__(name, False)

    def set_price(self, price) -> None:
        super().set_price(price)

    def get_pirce(self) -> float:
        super().get_pirce()

    def get_build_accessabled(self) -> bool:
        super().get_build_accessabled()

    def set_name(self, name) -> None:
        super().set_name(name)
    
    def get_name(self):
        super().get_name()


