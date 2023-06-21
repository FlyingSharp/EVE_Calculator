from construction.component.BasicComponent import BasicComponent
from construction.component.AdvancedComponent import AdvancedComponent

from construction.ship.conventionalship.freighter.Freighter import Freighter
from construction.ship.conventionalship.industory_ship.IndustoryCommderShip.IndustoryCommderShip import IndustoryCommderShip

from construction.ship.flagship.industory_flagship.IndustoryFlagShip import IndustoryFlagShip
from construction.ship.flagship.strategic_freighter.StrategicFreighter import StrategicFreighter
from construction.ship.flagship.carrier.supercarrier.SuperCarrier import SuperCarrier

import ConvertItemTree

class Factory:
    item_classes = {
        "基础组件": BasicComponent,
        "高级组件": AdvancedComponent,
        "货舰": Freighter,
        "旗舰级工业舰": IndustoryFlagShip,
        "战略货舰": StrategicFreighter,
        "超级航母": SuperCarrier,
        "工业指挥舰": IndustoryCommderShip,
    }

    __obj_created_list = [] # 已经创建过的obj列表

    def create_item(self, item_name: str):
        if item_name is None:
            print("没有输入物品名称")
            return None
        item_class_name = ConvertItemTree.ConvertItemTree().get_class_name(item_name)
        if item_class_name is None:
            print("没有找到物品分类")
            return None
        cls = self.item_classes.get(item_class_name.lower())
        if cls is None:
            print("没有找到物品分类对应的类名称")
            return None
        
        obj_item = None
        matching_items = [item for item in self.__obj_created_list if item.name == item_name]
        if len(matching_items) == 0:
            obj_item = cls(item_name)
            self.__obj_created_list.insert(len(self.__obj_created_list), obj_item)
        else: obj_item = matching_items[0]

        return obj_item


