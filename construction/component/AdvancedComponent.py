from construction.component.Component import Component


class AdvancedComponent(Component):


    def __init__(self, name: str) -> None:
        super().__init__(name)
        self._manufacture_available = False
        self.__name_in_tree = "高级组件"
        self.__extra_mat_influence = 0

    def get_material_list(self) -> None:
        return None

    def get_skill_influence(self) -> None:
        return None

    def get_final_material_list(self) -> None:
        return None
