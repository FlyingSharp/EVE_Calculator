import locale

import Factory
import ConvertItemTree
from construction.Item import Item
from price.GetPrice import GetPrice


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

    return currency_string[::-1].replace(",", ".", 1)[::-1]


def __get_mat_with_layer(need_prepare_mat, mat_in_layers, layer_count, item_name, item_count, manufacturing_costs_stack, manufacture_count):
    item = Factory.Factory().create_item(item_name)
    if item.get_manufacture_available():
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
            __get_mat_with_layer(need_prepare_mat, mat_in_layers, layer_count + 1, mat_name, mat_count, manufacturing_costs_stack, item_count)
    else:  # 如果创建不出来，说明是最基础的材料了
        update_dict(need_prepare_mat, {item_name: item_count * manufacture_count})


def get_mat(order_list, order_count):
    need_prepare_mat = {}  # 所有需要准备的材料

    mat_in_layers = {}
    layer_count = 0
    manufacturing_costs_stack = []

    for item_name, item_count in order_list.items():
        # 递归执行获得制造材料
        __get_mat_with_layer(need_prepare_mat, mat_in_layers, layer_count, item_name, item_count, manufacturing_costs_stack, order_count)

    out_str = f"订单数量: order_count\n订单详情:\n"
    for item_name, item_count in order_list.items():
        out_str += f"\t{item_name}:{item_count}\n"

    out_str += "\n所有需要准备的材料:\n"
    for k, v in need_prepare_mat.items():
        out_str += f"\t{k}:{v}\n"

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

    # 订单内容
    order_list = {
        "奥鸟级": 1,
    }

    order_count = 1  # 订单数量

    materials_string = get_mat(order_list, order_count)
    print(materials_string)


if __name__ == "__main__":
    main()