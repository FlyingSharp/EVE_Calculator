class Item:
    __name_in_tree = "物品"
    __skill_path = "industory_skill/skill.config"
    _material_list = None

    def __init__(self, name: str) -> None:
        self.name = name
    
    def get_material_list(self) -> dict:
        if not self._material_list:
            pass # 获取材料列表
        return self._material_list

    def get_skill_influece(self):
        # 获取技能影响因子
        material_influence = 0
        time_influence = 0

        return material_influence, time_influence
    
    def get_final_material_list(self) -> dict:
        material_influence, time_influence = self.get_skill_influece()
        material_list = self.get_material_list()
        for material_name, count in material_list:
            material_list[material_name] = count * (1 + material_influence)
        
        return material_list