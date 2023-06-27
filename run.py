import locale

import Factory
import ConvertItemTree
from construction.Item import Item
from price.GetPrice import GetPrice

def get_currency_string(f_all_price):
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
    # 获取当前环境下的小数点符号和千位分隔符
    decimal_point = locale.localeconv()['decimal_point']
    thousands_sep = locale.localeconv()['thousands_sep']

    # 将数字转换为货币格式的字符串，并去掉货币符号
    currency_string = '{:,.2f}'.format(f_all_price).replace(decimal_point, thousands_sep)

    return currency_string

def format_material_list(item_obj) -> str:
    assert item_obj is not None, "item_obj 不能为空！"
    item_obj_name = item_obj.name
    out_str = f"{item_obj_name}:\n"
    material_list = item_obj.get_final_material_list().items() #{ mat_1 = 15, mat_2 = 3}
    for k, v in material_list:
        out_str += f"\t{k}:{v}\n"

    # 暂时就先写最多两层的制造材料吧，任意多层的，以后再弄吧
    mineral_list = {}
    need_strench = False
    for k, v in material_list:
        sub_item = Factory.Factory().create_item(k)
        if sub_item:  # 例如: 如果找到了 一个组件
            sub_material_list = sub_item.get_final_material_list() # 获得组件材料 如: 三钛合金:1000
            if not sub_material_list: # 如果是不可制造的高级物品（非基础矿物），跳过材料列表
                continue
            for sub_k, sub_v in sub_material_list.items():  # 遍历材料名称，加入总材料列表   三钛合金:1000
                need_strench = True
                if sub_k in mineral_list: # 如果已经加过三钛合金了
                    mineral_list[sub_k] += sub_v * v # 组件所需的基础材料 * 所需组件数量
                else:
                    mineral_list[sub_k] = sub_v * v
        elif v not in mineral_list.keys():# 如果没找到，并且不在已经列出的材料列表里，就添加进去
            mineral_list[k] = v
    if need_strench:
        out_str += "各项基础材料总计:\n"
        for k, v in mineral_list.items():
            out_str += f"\t{k}:{v}\n"

    f_all_price = 0.0
    for k, v in mineral_list.items(): # 遍历各项基础材料价格总计
        price = GetPrice().get_price(k)
        f_all_price += price * v

    currency_string = get_currency_string(f_all_price)[::-1].replace(",", ".", 1)[::-1]
    out_str += f"\n材料价格总计:\n{currency_string}"

    return out_str

def __get_mat_with_layer(mat_in_layers, layer_count, item_name, item_count):
    item = Factory.Factory().create_item(item_name)
    if item:
        material_list_pack = item.get_final_material_list()  # 获得组件材料 如: 三钛合金:1000 { mat_1 = 15, mat_2 = 3}
        material_list = {}
        if material_list_pack:
            material_list = material_list_pack.items()
        # 这边应该检查这一层是否还没有初始化；如果没有，就以当前material_list初始化为一个字典；如果已经初始化了，就在当前的material_list和这一层的键中检索是否已经存在，如果已经存在在这一层的键中，就更新这个键的值
        if layer_count not in mat_in_layers:
            mat_in_layers[layer_count] = {}
        for mat_name, mat_count in material_list:
            if mat_name not in mat_in_layers[layer_count]:
                mat_in_layers[layer_count][mat_name] = 0
            mat_in_layers[layer_count][mat_name] += mat_count

        for mat_name, mat_count in material_list:
            __get_mat_with_layer(mat_in_layers, layer_count + 1, mat_name, mat_count)

def get_mat(item_name, item_count):
    mat_in_layers = {}
    layer_count = 0

    # 递归执行获得制造材料
    __get_mat_with_layer(mat_in_layers, layer_count, item_name, item_count)

    out_str = f"{item_name}所需材料:\n"
    for k, v in mat_in_layers[0].items():
        out_str += f"\t{k}:{v}\n"
    if len(mat_in_layers) > 1:
        out_str += "所有基本材料：\n"
        for k, v in mat_in_layers[len(mat_in_layers) - 1].items():
            out_str += f"\t{k}:{v}\n"

    return out_str

def main():
    item_name = "冥府级"
    item_count = 1

    # item_obj = Factory.Factory().create_item(item_name)
    #
    # all_material = format_material_list(item_obj)
    # print(all_material)

    materials_string = get_mat(item_name, item_count)
    print(materials_string)

if __name__ == "__main__":
    main()