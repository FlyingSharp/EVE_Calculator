from extra_buffer.singleton import singleton

@singleton
class CompanySkillsEffect:
    def __init__(self):
        self.__conventional_obj = ConventionalShipEffect()
        self.__flagship_obj = FlagshipEffect()

    def get_company_skills_effect(self):
        conventioal_effect = self.__conventional_obj.get_effect()
        flagship_effect = self.__flagship_obj.get_effect()

        return conventioal_effect + flagship_effect


@singleton
class ConventionalShipEffect:
    def __init__(self, level):
        assert level <= 1
        level_effect = [-0.003]
        self.__material_influence = level_effect[level - 1]

    def get_effect(self):
        return self.__material_influence

@singleton
class FlagshipEffect:
    def __init__(self, level):
        assert level <= 1
        level_effect = [-0.004]
        self.__material_influence = level_effect[level - 1]

    def get_effect(self):
        return self.__material_influence