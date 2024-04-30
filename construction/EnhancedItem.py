from construction.Item import Item
from skill.GetSkillEffect import GetSkillEffect
import MySkill


class EnhancedItem(Item):

    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.__name_in_tree = "增强物品"
        self.__extra_mat_influence = 0

    def get_single_skill_influence(self, item_relate_skills):
        material_influence = 0
        time_influence = 0

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

        return material_influence + self.__extra_mat_influence, time_influence

    def get_skill_influence(self):
        super_material_influence, super_time_influence = super().get_skill_influence()
        material_influence, time_influence = self.get_single_skill_influence(
            GetSkillEffect().get_skill_name_by_item_name(self.__name_in_tree))

        print(self.__name_in_tree + f"material_influence:{material_influence}")
        return material_influence + super_material_influence, time_influence + super_time_influence
