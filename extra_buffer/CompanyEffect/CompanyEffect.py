from extra_buffer.singleton import singleton
from extra_buffer.CompanyEffect.company_branches.CompanyBuildingEffect import CompanyBuildingEffect
from extra_buffer.CompanyEffect.company_branches.CompanySkillsEffect import CompanySkillsEffect

@singleton
class CompanyEffect():
    def __init__(self):
        self.__company_building_effect_cls_obj = CompanyBuildingEffect()
        self.__company_skills_effect_cls_obj = CompanySkillsEffect()

    def get_company_material_effect(self):
        building_effect = 0
        skills_effect = 0

        return  building_effect + skills_effect