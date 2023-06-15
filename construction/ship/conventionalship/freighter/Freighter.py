import Ship

class Freighter(Ship):
    __name_in_tree = "货舰"
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def get_material_list(self) -> dict:
        super().get_material_list()

    def get_skill_influece(self):
        super_material_influence, super_time_influence = super().get_skill_influece()

        this_material_influece = 0
        this_time_influence = 0

        final_material_influence = super_material_influence + this_material_influece
        final_time_influence = super_time_influence + this_time_influence

        return final_material_influence, final_time_influence