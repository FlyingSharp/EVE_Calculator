from construction.component.Component import Component

class AdvancedComponent(Component):
    __name_in_tree = "高级组件"
    __manufacturing_costs = 0.0
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.__config_path = self._get_config_path()

    def get_material_list(self) -> dict:
        return None
    
    def get_skill_influece(self):
        return None

    def get_final_material_list(self) -> None:
        return None