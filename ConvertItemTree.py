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
        self.__convert_to_dict()

    def __convert_to_dict(self):
        filename = "items_tree.config"
        with open(filename, "r") as f:
            text = f.read()
        result = {}
        stack = [result]
        for line in text.split("\n"):
            name, _, _ = line.strip().partition(" ")
            depth = len(name) - len(name.lstrip())
            node = name.strip()
            while depth + 1 < len(stack):
                stack.pop()
            parent = stack[-1]
            if type(parent) == dict:
                parent[node] = {}
            else:
                parent.append(node)
            stack.append(parent[node])
        
        self.__item_tree = result

    def get_class_name(self, item_name):
        def get_name(dic, item_name):
            """""
            Args:
                dic: 待查找的字典
                leaf_name: 叶子节点名称
            
            Returns:
                查找成功时返回对应的键名称，否则返回None
            """
            for key, value in dic.items():
                if isinstance(value, list):
                    if item_name in value:
                        return key
                elif isinstance(value, dict):
                    sub_key = get_name(value, item_name)
                    if sub_key is not None:
                        return sub_key
            return None
        
        return get_name(self.__item_tree, item_name)