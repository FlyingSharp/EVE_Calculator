def singleton(cls):
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

@singleton
class ConvertItemTree:
    __item_tree = None

    def __init__(self) -> None:
        # self.__convert_to_dict()
        self.__item_tree = {
            "基础组件": [
                "旗舰船只维护舱",
                "旗舰电容器电池",
                "旗舰发电机组",
                "旗舰发射器安装座",
                "旗舰附甲",
                "旗舰感应器组",
                "旗舰护盾发射器",
                "旗舰会战能源阵列",
                "旗舰货柜舱",
                "旗舰计算机系统",
                "旗舰建设构件",
                "旗舰克隆舱",
                "旗舰联合机库舱",
                "旗舰末日武器安装位",
                "旗舰炮台挂点",
                "旗舰跳跃桥接阵列",
                "旗舰跳跃引擎",
                "旗舰推进引擎",
                "旗舰无人机挂舱"
            ],
            "高级组件": [
                "神经链接回路",
                "神经链接防护单元",
                "超光速链接通信器",
                "核心结构自动修复装置",
                "生命保障装置",
                "核心温度调节系统"
            ],
            "无畏舰":[
                "凤凰级"
            ],
            "航空母舰": {
                "冥府级",
                "飞龙级",
                "万古级",
                "夜神级"
            },
            "旗舰级工业舰": {
                "长须鲸级"
            },
            "战略货舰": {
                "奥鸟级",
                "方舟级",
                "游牧者级",
                "安莎尓级"
            },
            "战力辅助舰": {
                "龙鸟级"
            },
            "货舰": {
                "渡神级",
                "普罗维登斯级",
                "芬利厄级",
                "方尖塔级"
            }
        }

    def __convert_to_dict(self):
        filename = "items_tree.config"
        with open(filename, "r") as f:
            text = f.read()

        lines = text.strip().split("\n")
        result = {}
        stack = [result]
        prev_indent = 0

        for line in lines:
            indent_level = len(line) - len(line.lstrip())
            node_name = line.strip()

            if not node_name:
                continue

            node = {node_name: {}}

            if indent_level > prev_indent:
                stack[-1][prev_node].update(node)
                stack.append(stack[-1][prev_node])
            elif indent_level < prev_indent:
                while len(stack) > 1 and prev_indent - indent_level < (len(stack) - 1) * 4:
                    stack.pop()
                stack[-1].update(node)
            else:
                stack[-1].update(node)

            prev_node = node_name
            prev_indent = indent_level
        
        self.__item_tree = result

    def find_path(self, dict, item_name):
        for k, v in d.items():
            if isinstance(v, dict) and not bool(v):
                if k == s:
                    return ""
            elif isinstance(v, dict):
                result = self.find_path(v, s)
                if result is not None:
                    if result == "":
                        return k
                    else:
                        return k + "/" + result
        return None

    def get_last_component(self, s):
        index = s.rfind("/")
        if index == -1:
            return s
        else:
            return s[index + 1:]

    def get_class_name(self, item_name):
        # item_path = self.find_path(self.__item_tree, item_name)
        # if not item_path:
        #     return  None
        # class_name = self.get_last_component(item_path)
        # return class_name
        for key, value in self.__item_tree.items():
            if item_name in value:
                print(f"找到{item_name}")
                return key
        return None