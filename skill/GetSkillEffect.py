import os
import re

def singleton(cls):
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

@singleton
class GetSkillEffect:
    __skill_Dictionary = None
    __skill_influent_items_Dictionary = None

    def __init__(self):
        pass

    def get_full_skill_effect(self, skill_path, skill_name: str):
        if not skill_name or skill_name == "":
            return None

        if not self.__skill_Dictionary or not self.__skill_Dictionary[skill_name]:
            # 解析技能列表，并缓存
            # {
            #     '货舰制造': {
            #         'basic': [(6, 5), (12, 10), (18, 15), (24, 20), (30, 25)],
            #         'advanced': [(6, 5), (12, 10), (18, 15), (24, 20), (30, 25)],
            #         'export': [(6, 5), (12, 10), (18, 15), (24, 20), (30, 25)]
            #     }
            # }
            try:
                skill_Dictionary = {}
                with open(skill_path, "r") as f:
                    input_str = f.read()

                    for line in input_str.split("\n"):
                        line = re.sub(r"\s", "", line)
                        if not line:
                            continue
                        if line.endswith(":"):
                            current_key = line[:-1]
                        else:
                            try:
                                subkey, values_str = line.strip().split(":", 1)
                                values = [
                                    [int(v) for v in value_str.replace(" ", "").lstrip("(").rstrip(")").split(",")] for
                                    value_str in values_str.split(",")]
                                skill_Dictionary.setdefault(current_key, {}).setdefault(subkey, []).extend(values)
                            except (ValueError, TypeError) as e:
                                print(f"行 {line} 格式不正确！无法分割")
                                continue

                    output_dict = {}
                    for category, items in skill_Dictionary.items():
                        output_dict[category] = {}
                        for item, values in items.items():
                            original_list = [value for sublist in values for value in sublist]
                            new_list = []
                            for i in range(0, len(original_list), 2):
                                new_list.append([original_list[i], original_list[i + 1]])

                            output_dict[category][item] = new_list

                if not self.__skill_Dictionary:
                    self.__skill_Dictionary = output_dict
                else:
                    self.__skill_Dictionary.update(output_dict) # 将新解析的拼接到原有的技能表上去
            except FileNotFoundError:
                print("文件不存在！")
                exit()
        
        # 已缓存完技能树
        index_dict = {"basic": 0, "advanced": 1, "export": 2}

        output_dict = {}
        for category, items in self.__skill_Dictionary.items():
            output_dict[category] = {}
            for key, values in items.items():
                for i in range(len(values)):
                    for j in range(len(values[i])):
                        values[i][j] *= -0.01
                output_dict[category][index_dict[key]] = values

        # rv = {
        # [[-0.06, -0.05], [-0.12, -0.10], [-0.18, -0.15], [-0.24, -0.20], [-0.30, -0.25]],
        # [[-0.06, -0.05], [-0.12, -0.10], [-0.18, -0.15], [-0.24, -0.20], [-0.30, -0.25]],
        # [[-0.06, -0.05], [-0.12, -0.10], [-0.18, -0.15], [-0.24, -0.20], [-0.30, -0.25]]
        # }
        return output_dict

    def get_skill_name_by_item_name(self, item_name):
        if not self.__skill_influent_items_Dictionary:
            try:
                with open("skill/skill_influent_items.config", 'r', encoding='utf-8') as f:
                    lines = [line for line in f.readlines() if not line.startswith("#")]
            except FileNotFoundError:
                print(os.path.join(os.path.dirname(os.path.abspath(__file__))), "skill_influent_items.config") + "不存在"
                exit()

            skill_influent_items_Dictionary = {}
            for line in lines:
                try:
                    key, value = line.strip().split(':')
                except ValueError:
                    print(f"行 {line} 格式不正确！没有:号")
                    continue
                skill_influent_items_Dictionary[key] = value

            self.__skill_influent_items_Dictionary = skill_influent_items_Dictionary
        
        skill_list = tuple(k for k, v in self.__skill_influent_items_Dictionary.items() if v == item_name)
        return skill_list
    
