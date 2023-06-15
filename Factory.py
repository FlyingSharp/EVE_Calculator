import construction.Item
import construction.component.BasicComponent as bc
import construction.component.AdvancedComponent as ac

import construction.ship.conventionalship.freighter.Freighter as freg

class Factory:
    item_classes = {
        "基础组件": bc.BasicComponent,
        "高级组件": ac.AdvancedComponent,
        "货舰": freg.Freighter
    }

    __obj_created_list = [] # 已经创建过的obj列表

    def create_item(self, item_name):
        cls = self.item_classes.get(item_name.lower())
        if cls is None:
            raise ValueError(f"Unknown item: {item_name}")
        
        obj_item = None
        matching_items = [item for item in self.__obj_created_list if item.name == "渡神级"]
        if len(matching_items) == 0:
            obj_item = cls(item_name)
            self.__obj_created_list.insert(len(self.__obj_created_list), obj_item)
        else: obj_item = matching_items[0]
        return obj_item

# 示例用法
# factory = Factory()
# item = factory.create_item("Ship")
# print(type(item))  # 输出：<class '__main__.Ship'>