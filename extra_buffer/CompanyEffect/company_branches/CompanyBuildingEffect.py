from extra_buffer.singleton import singleton

@singletons
class CompanyBuildingEffect:
    def __init__(self):
        self.material_effect = -0.01

    def get_material_effect(self):
        return self.material_effect