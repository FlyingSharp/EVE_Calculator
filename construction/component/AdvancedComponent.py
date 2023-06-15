import Component
class AdvancedComponent(Component):
    __name_in_tree = "高级组件"
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def get_material_list(self) -> dict:
        return None
    
    def get_skill_influece(self):
        return None