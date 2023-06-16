from construction.ship.conventionalship.ConventionalShip import ConventionalShip
from skill.GetSkillEffect import GetSkillEffect
import MySkill

import math

class Freighter(ConventionalShip):
    __name_in_tree = "货舰"
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.__config_path = self._get_config_path()

    def get_skill_influece(self):
        super_material_influence, super_time_influence = super().get_skill_influece()

        material_influence = 0
        time_influence = 0

        item_relate_skills = GetSkillEffect().get_skill_name_by_item_name(self.__name_in_tree)
        my_skill = MySkill.MySkill().skills
        for skill_name, skill_level in my_skill:
            if skill_name in item_relate_skills:
                skill_effect = GetSkillEffect().get_full_skill_effect(self.__skill_path, skill_name)
                for i in range(0, 2):
                    influence_tuple_list = skill_effect[i]
                    for k, v in influence_tuple_list:
                        material_influence += v[0]
                        time_influence += v[1]

        return material_influence + super_material_influence, time_influence + super_time_influence
    
    def get_final_material_list(self) -> dict:
        material_influence, time_influence = self.get_skill_influece()
        material_list = self.get_material_list()
        for material_name, count in material_list:
            material_list[material_name] = math.ceil( count * (1 + material_influence))
        
        return material_list