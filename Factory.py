from construction.component.BasicComponent import BasicComponent
from construction.component.AdvancedComponent import AdvancedComponent

from construction.ship.conventionalship.freighter.Freighter import Freighter

class Factory:
    item_classes = {
        "基础组件": BasicComponent.BasicComponent,
        "高级组件": AdvancedComponent.AdvancedComponent,
        "货舰": Freighter.Freighter
        # "旗舰级工业舰": 
    }

    __obj_created_list = [] # 已经创建过的obj列表

    def create_item(self, item_name):
        cls = self.item_classes.get(item_name.lower())
        if cls is None:
            return None
        
        obj_item = None
        matching_items = [item for item in self.__obj_created_list if item.name == item_name]
        if len(matching_items) == 0:
            obj_item = cls(item_name)
            self.__obj_created_list.insert(len(self.__obj_created_list), obj_item)
        else: obj_item = matching_items[0]

        return obj_item







# 示例用法
# factory = Factory()
# item = factory.create_item("Ship")
# print(type(item))  # 输出：<class '__main__.Ship'>