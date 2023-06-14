import json

class PathFinder:
    _instance = None

    def __new__(cls, file_path):
        if not cls._instance:
            cls._instance = super(PathFinder, cls).__new__(cls)
            with open(file_path, "r") as f:
                cls._instance.content = f.read()

            cls._instance.nojson_tree = {}
            lines = cls._instance.content.split('\n')
            current_level = 0
            stack = [cls._instance.nojson_tree]
            for line in lines:
                if not line.strip():
                    # Skip empty lines
                    continue
                level = len(line) - len(line.lstrip())
                value = line.strip()
                item = {value: {}}
                if level == current_level:
                    stack.pop()
                elif level < current_level:
                    for _ in range(current_level - level + 1):
                        stack.pop()
                stack[-1][list(stack[-1].keys())[0]].update(item)
                stack.append(item)
                current_level = level

            cls._instance.json_tree = json.dumps(cls._instance.nojson_tree, indent=4)
        return cls._instance

    # 返回的是一个 list，如果没找到就返回 None
    def find_path(self, item_name):
        def traverse(node, path):
            for key, value in node.items():
                if isinstance(value, dict):
                    traverse(value, path + [key])
                elif key == item_name:
                    path.append(path + [key])

        path = []
        traverse(self.json_tree, path)
        return path[0] if path else None