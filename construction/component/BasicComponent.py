from construction.component.Component import Component


class BasicComponent(Component):

    def __init__(self, name: str) -> None:
        super().__init__(name)
        self._name_in_tree = "基础组件"