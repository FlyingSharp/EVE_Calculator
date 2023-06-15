import skills.skill_main
import items.Item as Item
import items.FindItemPath
import items.component.Component as Component

def print_result(result: str):
    pass

def calculate_influence():
    pass

def calculate_material(item_tree_path, skill_effect, skill_effect_objects, my_skill):
    item_path_finder = items.FindItemPath()

    # 直接判断这个物品的内置材料是不是可建造的
    item_name = item_tree_path[-1]
    item_obj = Item()
    if "基础组件" in item_tree_path:
        item_obj = Component.BasicComponent(item_name)
    elif "高级组件" in item_tree_path:
        item_obj = Component.AdvancedComponent(item_name)

    if item_obj._material_dict:
        for material in item_obj._material_dict:
            if material._build_accessable:
                # 继续查看这个材料是不是还是可以被生产的
                pass
def main():
    # Item类 list
    searched_items = []

    item_path_finder = items.FindItemPath()
    
    while True:
        # 根据要建造的物品名称，找到该物品的原始图纸消耗
        item_name = input("请输入要查找的物品名称(输入 '__exit__' 退出程序)：")
        if item_name == "__exit__":
            break

        item_tree_path = item_path_finder.find_path(item_name) # 例: 物品 -> 组件 -> 基础组件 -> 旗舰货柜舱

        if not item_tree_path:
            print(f"没有找到{item_name}")
            break
            
        skill_effect, skill_effect_objects, my_skill = skills.skill_main.init_skill()
        calculate_material(item_tree_path, skill_effect, skill_effect_objects, my_skill)


        
        # 查找所有影响该物品的技能等级，返回影响因子
        ###                             skill_effect
            # {
            #     '货舰制造': {
            #         'basic': [(6, 5), (12, 10), (18, 15), (24, 20), (30, 25)],
            #         'advanced': [(6, 5), (12, 10), (18, 15), (24, 20), (30, 25)],
            #         'export': [(6, 5), (12, 10), (18, 15), (24, 20), (30, 25)]
            #     },
            #     '旗舰组件制造': {
            #         'basic': [(6, 5), (12, 10), (18, 15), (24, 20), (30, 25)],
            #         'advanced': [(4, 5), (8, 10), (12, 15), (16, 20), (20, 25)],
            #         'export': [(1, 5), (2, 10), (3, 15), (4, 20), (5, 25)]
            #     }
            # }
        ###

        

        # 检索所有其他附加条件的影响因子（军团堡垒、甜甜圈），返回影响因子

        # 总计所有影响因子，得到该物品的制造花费


    # while True:
        # item_name = input("请输入要查找的物品名称(输入 '__exit__' 退出程序)：")
        # if item_name == "__exit__":
        #     break
        # if item_name not in items:
        #     print("没有找到该物品，请重新输入！")
        #     continue
        # item_info = items[item_name]
        

if __name__ == "__main__":
    main()
