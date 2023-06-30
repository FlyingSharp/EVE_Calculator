from construction.component.Component import Component

class AdvancedComponent(Component):
    __name_in_tree = "高级组件"
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.__config_path = self._get_config_path()
        self.__manufacture_available = False

    def get_material_list(self) -> dict:
        return None
    
    def get_skill_influence(self):
        return None

    def get_final_material_list(self) -> None:
        return None

    def get_manufacturing_cost(self) -> float:
        return self.__manufacturing_costs

    def get_item_class_name(self):
        return self.__name_in_tree

    def get_manufacture_available(self):
        return self.__manufacture_available