import Factory
import ConvertItemTree

def format_material_list(item_obj):
    item_obj_name = item_obj.name
    out_str = f"{item_obj_name}:\n"
    material_list = item_obj.get_final_material_list() #{ mat_1 = 15, mat_2 = 3}
    for k, v in material_list:
        out_str += f"\t{k}:{v}\n"

    # 暂时就先写最多两层的制造材料吧，任意多层的，以后再弄吧
    mineral_list = {}
    need_strench = False
    for k, v in material_list:
        sub_item = Factory.Factory().create_item(ConvertItemTree.ConvertItemTree().get_class_name(k))
        if sub_item:  # 例如: 如果找到了 一个组件
            sub_material_list = sub_item.get_final_material_list() # 获得组件材料 如: 三钛合金:1000
            if not sub_material_list: # 如果是不可制造的高级物品（非基础矿物），跳过材料列表
                continue
            for sub_k, sub_v in sub_material_list:  # 遍历材料名称，加入总材料列表   三钛合金:1000
                if mineral_list.has_key(sub_k): # 如果已经加过三钛合金了
                    mineral_list[sub_k] += sub_v * v # 组件所需的基础材料 * 所需组件数量
                    need_strench = True
        else:
            mineral_list[k] = v
    if need_strench:
        out_str += "各项基础材料总计:\n"
    for k, v in mineral_list:
        out_str += f"\t{k}:{v}\n"

    return out_str

def main():
    item_name = "渡神级"
    item_class_name = ConvertItemTree.ConvertItemTree().get_class_name(item_name)
    item_obj = Factory.Factory().create_item(item_class_name)

    all_material = format_material_list(item_obj)
    print(all_material)


if __name__ == "__main__":
    main()