import os

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

    def __init__(self, value):
        self.value = value

    def get_full_skill_effect(self, skill_path, skill_name):
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
                    current_key = ""
                    for line in f.readlines():
                        # 去除每行两端的空格和换行符
                        line = line.strip()
                        # 忽略空行
                        if not line:
                            continue
                        # 判断是否为主键
                        if line.endswith(":"):
                            current_key = line[:-1]
                            skill_Dictionary[current_key] = {}
                        else:
                            # 判断是否为子键
                            if line.startswith(" "):
                                try:
                                    subkey, values_str = line.strip().split(": ")
                                    values = [tuple(map(int, v.strip("()").split(", "))) for v in values_str.split(", ")]
                                except (ValueError, TypeError) as e:
                                    print(f"行 {line} 格式不正确！无法分割")
                                    continue
                                skill_Dictionary[current_key][subkey] = values

                if not self.__skill_Dictionary:
                    self.__skill_Dictionary = skill_Dictionary
                else:
                    self.__skill_Dictionary.update(skill_Dictionary) # 将新解析的拼接到原有的技能表上去
            except FileNotFoundError:
                print("文件不存在！")
                exit()
        
        # 已缓存完技能树
        rv = {}
        subkeys = ["basic", "advanced", "export"]
        for i in len(self.__skill_Dictionary[skill_name]):
            rv[i] = self.__skill_Dictionary[skill_name][subkeys[i]]
        # rv = {
        # [(6, 5), (12, 10), (18, 15), (24, 20), (30, 25)],
        # [(6, 5), (12, 10), (18, 15), (24, 20), (30, 25)],
        # [(6, 5), (12, 10), (18, 15), (24, 20), (30, 25)]
        # }
        return rv

    def get_skill_name_by_item_name(self, item_name):
        if not self.__skill_influent_items_Dictionary:
            try:
                with open("skill_influent_items.config", 'r', encoding='utf-8') as f:
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
    
