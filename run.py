import locale

import Factory
import ConvertItemTree
from construction.Item import Item
from price.GetPrice import GetPrice
from construction.component.Component import Component
from construction.ship.Ship import Ship


def update_dict(dict_a: dict, dict_b: dict):
    for k, v in dict_b.items():
        if k not in dict_a:
            dict_a[k] = v
        else:
            dict_a[k] += v


def summery(array):
    sum = 0.0
    for v in array:
        sum += v
    return sum


def get_currency_string(currency):
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
    # 获取当前环境下的小数点符号和千位分隔符
    decimal_point = locale.localeconv()['decimal_point']
    thousands_sep = locale.localeconv()['thousands_sep']

    # 将数字转换为货币格式的字符串，并去掉货币符号
    currency_string = '{:,.2f}'.format(currency).replace(decimal_point, thousands_sep)
    #剔除最后三位（.00)
    currency_string = currency_string[::-1].replace(",", ".", 1)[::-1]
    currency_string = currency_string[:-3]

    return currency_string


def __get_mat_with_layer(need_prepare_mat, mat_in_layers, layer_count, item_name, item_count, manufacturing_costs_stack, manufacture_count, need_prepare_components):
    item = Factory.Factory().create_item(item_name)
    if item.get_manufacture_available():
        # 如果是组件类型，则加入need_prepare_components列表中
        if isinstance(item, Component):
            update_dict(need_prepare_components, {item_name: item_count})
        # 如果是舰船类型，也需要加入need_prepare_components列表中
        if isinstance(item, Ship):
            update_dict(need_prepare_components, {item_name: item_count})

        manufacturing_cost = item.get_manufacturing_cost() * item_count
        print(f"manufacturing_cost:{manufacturing_cost}")
        manufacturing_costs_stack.append(manufacturing_cost)
        material_list_pack = item.get_final_material_list()  # 获得组件材料 如: 三钛合金:1000 { mat_1 = 15, mat_2 = 3}
        material_list = {}
        if material_list_pack:
            material_list.update(material_list_pack.items())
        # 这边应该检查这一层是否还没有初始化；如果没有，就以当前material_list初始化为一个字典；如果已经初始化了，就在当前的material_list和这一层的键中检索是否已经存在，如果已经存在在这一层的键中，就更新这个键的值
        if layer_count not in mat_in_layers:
            mat_in_layers[layer_count] = {}
        for mat_name, mat_count in material_list.items():
            if mat_name not in mat_in_layers[layer_count]:
                mat_in_layers[layer_count][mat_name] = 0
            mat_in_layers[layer_count][mat_name] += mat_count * item_count  # mat_count：建造这个物品所需要的材料的数量   item_count：这个物品需要建造的数量

        for mat_name, mat_count in material_list.items():
            __get_mat_with_layer(need_prepare_mat, mat_in_layers, layer_count + 1, mat_name, mat_count, manufacturing_costs_stack, item_count, need_prepare_components)
    else:  # 如果创建不出来，说明是最基础的材料了
        update_dict(need_prepare_mat, {item_name: item_count * manufacture_count})


def get_mat(order_list, order_count):
    need_prepare_mat = {}  # 所有需要准备的材料
    need_prepare_components = {}  # 共计需要准备的组件数量

    mat_in_layers = {}
    layer_count = 0
    manufacturing_costs_stack = []

    for item_name, item_count in order_list.items():
        # 递归执行获得制造材料
        __get_mat_with_layer(need_prepare_mat, mat_in_layers, layer_count, item_name, item_count, manufacturing_costs_stack, order_count, need_prepare_components)

    out_str = f"订单数量: {order_count}\n订单详情:\n"
    for item_name, item_count in order_list.items():
        out_str += f"\t{item_name}:{get_currency_string(item_count)}\n"

    if len(need_prepare_components) > 0:
        out_str += "\n所有组件的数量:\n"
        for k, v in need_prepare_components.items():
            out_str += f"\t{k}:{get_currency_string(v)}\n"

    out_str += "\n所有需要准备的材料:\n"
    for k, v in need_prepare_mat.items():
        out_str += f"\t{k}:{get_currency_string(v)}\n"

    materials_costs = 0.0
    for k, v in need_prepare_mat.items():  # 遍历各项基础材料价格总计
        price = GetPrice().get_price(k)
        materials_costs += price * v

    materials_costs_string = get_currency_string(materials_costs)
    out_str += f"\n材料价格总计:\n{materials_costs_string}"

    # 制造手续费
    manufacturing_costs = summery(manufacturing_costs_stack)
    manufacturing_costs_string = get_currency_string(manufacturing_costs)
    out_str += f"\n制造手续费总计:\n{manufacturing_costs_string}"

    # 总计花费
    total_cost = materials_costs + manufacturing_costs
    out_str += f"\n总计花费:\n{get_currency_string(total_cost)}"

    return out_str


def main():

    # 大鱼组件清单
    dayu_list = {
        "旗舰船只维护舱": 12,
        "旗舰电容器电池": 5,
        "旗舰发电机组": 5,
        "旗舰附甲": 3,
        "旗舰感应器组": 4,
        "旗舰护盾发射器": 4,
        "旗舰货柜舱": 9,
        "旗舰计算机系统": 12,
        "旗舰建设构件": 17,
        "旗舰克隆舱": 12,
        "旗舰联合机库舱": 7,
        "旗舰跳跃引擎": 5,
        "旗舰推进引擎": 4,
        "旗舰无人机挂舱": 3,
    }

    # 订单内容
    order_list = {
        # "奥鸟级": 1,
        # "渡神级": 1,

        # "专家旗舰装备发明核心理论": 1

        "蝠鲼重型采掘者无人机": 5
        # "突击型掷矛手": 1
    }

    order_count = 1  # 订单数量

    materials_string = get_mat(order_list, order_count)
    print(materials_string)


if __name__ == "__main__":
    main()