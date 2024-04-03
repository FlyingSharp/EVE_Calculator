import os
import glob


def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance


@singleton
class GetPrice:
    __paths = []
    __price_data = {}
    __mat_group = {}

    def __init__(self):
        self.__find_all_path()

        for path in self.__paths:
            # 打开文件并读取内容
            with open(path, 'r', encoding='UTF-8') as f:
                content = f.read()
            lines = content.split('\n')
            # 定义一个空字典用于存储解析后的数据
            price_data = {}
            # 存储每种材料的分类
            mat_group = {}
            group_key = path.split('/')[-2]
            mat_group[group_key] = []
            # 遍历每一行数据并解析
            for line in lines:
                # 如果这一行是空行则跳过
                if not line:
                    continue
                # 按冒号分隔这一行的数据，并去掉两端的空格
                parts = line.split(':')
                key = parts[0].strip()
                value = float(parts[1].strip())
                # 将解析出来的键值对添加到字典中
                price_data[key] = value
                mat_group[group_key].append(key)

            self.__price_data.update(price_data)
            self.__mat_group.update(mat_group)

    def __find_all_path(self):
        # 获取当前脚本所在的目录
        current_path = os.path.dirname(os.path.abspath(__file__))
        folder_list = os.listdir(current_path)
        for folder in folder_list:
            folder_path = os.path.join(current_path, folder)
            if not os.path.isdir(folder_path):
                continue
            pattern = os.path.join(folder_path, 'price.config')
            folder_paths = glob.glob(pattern)
            self.__paths.extend(folder_paths)

    def __str__(self):
        return str(self.__paths) + '\n' + str(self.__price_data)

    def get_price(self, name):
        return 0 if name not in self.__price_data else self.__price_data[name]

    def get_mat_group(self, mat_name):
        group_name = "未知类型, 材料名称：" + mat_name
        for k, v in self.__mat_group.items():
            try:
                index = v.index(mat_name)
            except ValueError:
                continue
            else:
                group_name = k
        return group_name





if __name__ == "__main__":
    print(GetPrice())
