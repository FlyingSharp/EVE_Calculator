from construction.ship.flagship.carrier.Carrier import Carrier
from skill.GetSkillEffect import GetSkillEffect


class SuperCarrier(Carrier):

    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.__name_in_tree = "超级航母"
        self._manufacturing_costs = 5000000000
        self.__extra_mat_influence = 0


    def get_skill_influence(self):
        super_material_influence, super_time_influence = super().get_skill_influence()
        material_influence, time_influence = self.get_single_skill_influence(
            GetSkillEffect().get_skill_name_by_item_name(self.__name_in_tree))

        print(self.__name_in_tree + f"material_influence:{material_influence}")
        return material_influence + super_material_influence, time_influence + super_time_influence
