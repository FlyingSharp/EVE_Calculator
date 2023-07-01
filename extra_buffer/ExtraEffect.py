from extra_buffer.singleton import singleton
from extra_buffer.CompanyEffect.CompanyEffect import CompanyEffect

@singleton
class ExtraEffect:
    def __init__(self):
        self._material_influence = CompanyEffect()
    def get_material_influence(self):
        return self._material_influence