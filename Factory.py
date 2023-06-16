from construction.component.BasicComponent import BasicComponent
from construction.component.AdvancedComponent import AdvancedComponent

from construction.ship.conventionalship.freighter.Freighter import Freighter
from construction.ship.flagship.industory_flagship.IndustoryFlagShip import IndustoryFlagShip

import ConvertItemTree

class Factory:
    item_classes = {
        "基础组件": BasicComponent,
        "高级组件": AdvancedComponent,
        "货舰": Freighter,
        "旗舰级工业舰": IndustoryFlagShip,
    }

    __obj_created_list = [] # 已经创建过的obj列表

    def create_item(self, item_name: str):
        if item_name is None:
            return None
        item_class_name = ConvertItemTree.ConvertItemTree().get_class_name(item_name)
        if item_class_name is None:
            return None
        cls = self.item_classes.get(item_class_name.lower())
        if cls is None:
            return None
        
        obj_item = None
        matching_items = [item for item in self.__obj_created_list if item.name == item_name]
        if len(matching_items) == 0:
            obj_item = cls(item_name)
            self.__obj_created_list.insert(len(self.__obj_created_list), obj_item)
        else: obj_item = matching_items[0]

        return obj_item


