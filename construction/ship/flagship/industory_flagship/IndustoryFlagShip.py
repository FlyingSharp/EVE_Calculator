from typing import Any
from construction.ship.flagship.Flagship import Flagship
from skill.GetSkillEffect import GetSkillEffect
import MySkill

import math

class IndustoryFlagShip(Flagship):
    __name_in_tree = "旗舰级工业舰"
    __manufacturing_costs = 3500000000
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.__config_path = self._get_config_path()

    def get_skill_influece(self):
        super_material_influence, super_time_influence = super().get_skill_influece()

        material_influence = 0
        time_influence = 0

        item_relate_skills = GetSkillEffect().get_skill_name_by_item_name(self.__name_in_tree)
        my_skill = MySkill.MySkill().skills
        for skill_name, skill_level in my_skill.items():
            if skill_name in item_relate_skills:
                skill_effect = GetSkillEffect().get_full_skill_effect(self._skill_path, skill_name)
                effect_self_skill = skill_effect[skill_name]
                for i in range(0, 3):
                    influence_tuple_list = effect_self_skill[i]

                    inner_level = skill_level[i] - 1
                    material_influence += influence_tuple_list[inner_level][0]
                    time_influence += influence_tuple_list[inner_level][1]

        return material_influence + super_material_influence, time_influence + super_time_influence
    
    def get_final_material_list(self) -> dict:
        material_influence, time_influence = self.get_skill_influece()
        all_material_list = self.get_material_list()
        material_list = {}
        out_list = {}
        if self.name in all_material_list:
            material_list = all_material_list[self.name].items()

        for material_name, count in material_list:
            out_list[material_name] = math.ceil( count / 1.5 * (1.5 + material_influence))
        
        return out_list