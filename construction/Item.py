import os
import re
import inspect
import math

import skill.GetSkillEffect
import MySkill

class Item:
    __name_in_tree = "物品"
    __skill_path = "industory_skill/skill.config"
    __config_path = None

    _material_list = None

    def __init__(self, name: str) -> None:
        self.name = name
        self.__config_path = self._get_config_path()

    def _get_config_path(self):
        # 获取调用该方法的类的文件路径
        file_path = inspect.getfile(self.__class__)
        # 获取该类所在目录的路径
        dir_path = os.path.dirname(file_path)
        # 组合成配置文件的完整路径
        config_path = os.path.join(dir_path, 'material.config')
        return config_path

    def get_material_list(self) -> dict:
        if not self._material_list:
            # define the regex pattern for matching each line of the file
            pattern = r"(\w+):\s*(\d+)"
            mat_list = {}
            with open(self.__config_path, 'r') as f:
                current_category = None # initialize the current category to None
                for line in f:
                    line = line.strip() # remove any leading/trailing whitespaces
                    if not line: # skip empty lines
                        continue
                    match = re.match(pattern, line) # check if the line matches the pattern
                    if match:
                        key = match.group(1)
                        value = int(match.group(2))
                        if current_category is None:
                            current_category = key
                            mat_list[current_category] = {}
                        mat_list[current_category][key] = value
                    else:
                        current_category = line
                        mat_list[current_category] = {}
            self._material_list = mat_list
        return self._material_list

    def get_skill_influece(self):
        material_influence = 0
        time_influence = 0

        item_relate_skills = skill.GetSkillEffect.GetSkillEffect.get_skill_name_by_item_name(self.__name_in_tree) # ("旗舰船只制造")
        my_skill = MySkill.MySkill().skills # 我有的技能  {"货舰制造" = [5, 5, 5]}
        for skill_name, skill_level in my_skill:
            if skill_name in item_relate_skills:
                skill_effect = skill.GetSkillEffect.GetSkillEffect.get_full_skill_effect(self.__skill_path, skill_name)
                # [[-0.06, -0.05], [-0.12, -0.10], [-0.18, -0.15], [-0.24, -0.20], [-0.30, -0.25]],
                # [[-0.06, -0.05], [-0.12, -0.10], [-0.18, -0.15], [-0.24, -0.20], [-0.30, -0.25]],
                # [[-0.06, -0.05], [-0.12, -0.10], [-0.18, -0.15], [-0.24, -0.20], [-0.30, -0.25]]
                for i in range(0, 2):
                    influence_tuple_list = skill_effect[i]
                    for k, v in influence_tuple_list:
                        material_influence += v[0]
                        time_influence += v[1]

        return material_influence, time_influence
    
    def get_final_material_list(self) -> dict:
        material_influence, time_influence = self.get_skill_influece()
        material_list = self.get_material_list()
        for material_name, count in material_list:
            material_list[material_name] = math.ceil( count * (1 + material_influence))
        
        return material_list
    
    def get_item_class_name(self):
        return self.__name_in_tree