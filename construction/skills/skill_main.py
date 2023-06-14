import Skill
import json

def parsing_skill_info(filepath):
    try:
        data = {}
        with open(filepath, "r") as f:
            current_key = ""
            for line in f.readlines():
                # 去除每行两端的空格和换行符
                line = line.strip()
                # 忽略空行
                if not line:
                    continue
                # 判断是否为主键
                if line.endswith(":"):
                    current_key = line[:-1]
                    data[current_key] = {}
                else:
                    # 判断是否为子键
                    if line.startswith(" "):
                        try:
                            subkey, values_str = line.strip().split(": ")
                            values = [tuple(map(int, v.strip("()").split(", "))) for v in values_str.split(", ")]
                        except (ValueError, TypeError) as e:
                            print(f"行 {line} 格式不正确！无法分割")
                            continue
                        data[current_key][subkey] = values

        return data
    except FileNotFoundError:
        print("文件不存在！")
        exit()

def parsing_skill_effect_objects(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("文件不存在！")
        exit()

    data = {}
    for line in lines:
        try:
            key, value = line.strip().split(':')
        except ValueError:
            print(f"行 {line} 格式不正确！没有:号")
            continue
        data[key] = value

    return data

def parsing_my_skill(file_path):
    data = {}
    with open(file_path, "r") as f:
        for line in f:
            key, values = line.strip().split(":")
            nums = [int(x) for x in values.split()]
            if nums[0] < 4:
                if nums[1] > 0:
                    raise Exception("进阶技能大于0的时候，基础技能不能小于4")
            if nums[1] < 5:
                if nums[2] > 0:
                    raise Exception("专家技能大于0的时候，进阶技能不能小于5")
            data[key] = nums

    return data

# def dump_with_json(self, data):
#     with open("skill_json.json", "w") as f:
#         json.dump(data, f, indent=4)

def init_skill():
    # 解析技能效果信息
    skill_effect = parsing_skill_info("skill.config")
    # 解析技能对生效的物体
    skill_effect_objects = parsing_skill_effect_objects("skill2items.config")
    # 解析自己的拥有的技能等级
    my_skill = parsing_my_skill("my_skill.config")

    return skill_effect, skill_effect_objects, my_skill