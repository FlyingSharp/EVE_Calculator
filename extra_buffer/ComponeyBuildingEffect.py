def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance


@singleton
class ComponeyBuildingEffect:
    def __init__(self):
        self.material_effect = -0.01

    def get_material_effect(self):
        return self.material_effect