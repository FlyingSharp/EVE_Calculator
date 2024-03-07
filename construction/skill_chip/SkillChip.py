from construction.EnhancedItem import EnhancedItem


class SkillChip(EnhancedItem):

    def __init__(self, name: str) -> None:
        super().__init__(name)
        self._name_in_tree = "技能芯片"
        self._manufacturing_costs = 25000000

    def get_extra_material_influence(self) -> float:
        # return BufferData.gear_material_influence
        return 0
