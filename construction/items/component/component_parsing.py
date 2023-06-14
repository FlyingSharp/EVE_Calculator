import json

def parse_text(text):
    result = {}
    components = text.split("\n")
    stack = []  # 用列表模拟堆栈，记录当前解析到的父级标题
    for i in range(len(components)):
        component = components[i].strip()
        if len(component) == 0:
            continue
        level = 0
        while component[level] == " ":  # 统计缩进空格数
            level += 1
        level //= 4  # 将空格数转换为层数
        name = component[level*4:].strip()  # 把标题内容提取出来
        if level == 0:
            result[name] = {}
            stack = [name]  # 重置堆栈
        else:
            parent = stack[level-1]
            while len(stack) > level:  # 弹出多余的父级标题
                stack.pop()
            stack.append(name)  # 添加当前标题到堆栈
            node = result[parent]
            for j in range(1, level):  # 找到当前标题的父节点
                node = node[stack[j]]
            node[name] = {}  # 在父节点中添加当前标题
    return json.dumps(result, indent=4)

