import re
import json
import os

class Consume():
    "这个类是为了解析存放在各个路径中的各个物品所需的材料配置文件"
    existing_names = set()

    def __init__(self, config_name: str):
        if config_name in Consume.existing_names:
            raise ValueError(f"config_name {config_name} is already taken")
        self.config_name = config_name.lower()
        Consume.existing_names.add(config_name)

    def parsing(self):
        cwd = os.getcwd()
        files = []
        for item in os.listdir(cwd):
            # 判断是否是一个文件，并且后缀名为 .config
            if os.path.isfile(os.path.join(cwd, item)) and item.endswith('.config'):
                files.append(item)
        

        file_name = ""
        for config_name in item:
            if config_name == self.config_name:
                file_name = config_name
                break
        
        # define the regex pattern for matching each line of the file
        pattern = r"(\w+):\s*(\d+)"
        # create an empty dictionary to store key-value pairs
        data = {}
        with open(file_name, 'r') as f:
            current_category = None # initialize the current category to None
            for line in f:
                line = line.strip() # remove any leading/trailing whitespaces
                if not line: # skip empty lines
                    continue
                match = re.match(pattern, line) # check if the line matches the pattern
                if match:
                    key = match.group(1)
                    value = int(match.group(2))
                    if current_category is None:
                        current_category = key
                        data[current_category] = {}
                    data[current_category][key] = value
                else:
                    current_category = line
                    data[current_category] = {}

        return data