from construction.ship.conventionalship.ConventionalShip import ConventionalShip
from skill.GetSkillEffect import GetSkillEffect


class IndustryShip(ConventionalShip):

    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.__name_in_tree = "工业舰"
        self.__extra_mat_influence = 0

    
    def get_skill_influence(self):
        super_material_influence, super_time_influence = super().get_skill_influence()
        material_influence, time_influence = self.get_single_skill_influence(GetSkillEffect().get_skill_name_by_item_name(self.__name_in_tree))

        print(self.__name_in_tree + f"material_influence:{material_influence}")
        return material_influence + super_material_influence, time_influence + super_time_influence