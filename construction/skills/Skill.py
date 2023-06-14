import parsing as config_parsing

class Skill:
    def __init__(self, name, inner_level = 0, outer_level = 0):
        self.name = name
        self.inner_level = inner_level
        self.outer_level = outer_level
        self.material_efficiency = 0
        self.time_efficiency = 0

        skill_effect = config_parsing.parsing2json("skill.config")
        outer_level_string_list = ["basic", "advanced", "export"]
        outer_level_string = outer_level_string_list[self.outer_level]
        
        self.material_efficiency = skill_effect.name[outer_level_string][self.inner_level][0]
        self.time_efficiency = skill_effect.name[outer_level_string][self.inner_level][0]

    def effect(self):
        return self.material_efficiency, self.time_efficiency


class OrdinarySkill(Skill):
    def __init__(self, name="null", inner_level=0) -> None:
        super().__init__(name, inner_level, 0)

    def effect(self):
        return super().effect()

class AdvancedSkill(Skill):
    def __init__(self, name="null", inner_level=0) -> None:
        super().__init__(name, inner_level, 1)

    def effect(self):
        return super().effect()

class ExportSkill(Skill):
    def __init__(self, name="null", inner_level=0) -> None:
        super().__init__(name, inner_level, 2)
    def effect(self):
        return super().effect()


class PresentSkill:
    def __init__(self, name, inner_level_list = [0,0,0]):
        self.name = name
        for index in range(len(inner_level_list)):
            if index == 0:
                self.ordinary = OrdinarySkill(name, inner_level_list[index])
            elif index == 1:
                self.advanced = AdvancedSkill(name, inner_level_list[index])
            elif index == 2:
                self.export = ExportSkill(name, inner_level_list[index])

    def set_effect_object():
        pass

    def effect(self):
        material_efficiency = 0
        time_efficiency = 0

        material_efficiency = self.ordinary.material_efficiency + self.advanced.material_efficiency + self.export.material_efficiency
        time_efficiency = self.ordinary.time_efficiency + self.advanced.time_efficiency + self.export.time_efficiency

        return material_efficiency, time_efficiency