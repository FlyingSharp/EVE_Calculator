from construction.ship.Ship import Ship
from extra_buffer.BufferData import BufferData
from skill.GetSkillEffect import GetSkillEffect


class ConventionalShip(Ship):

    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.__name_in_tree = "常规舰船"
        self.__extra_mat_influence = BufferData.conventional_ship_material_influence

    
    def get_skill_influence(self):
        super_material_influence, super_time_influence = super().get_skill_influence()
        material_influence, time_influence = self.get_single_skill_influence(GetSkillEffect().get_skill_name_by_item_name(self.__name_in_tree))

        print(self.__name_in_tree + f"material_influence:{material_influence}")
        return material_influence + super_material_influence, time_influence + super_time_influence