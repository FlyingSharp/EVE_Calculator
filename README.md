Author: 阿塔尼斯.雷诺

Use:
    在myskill.config中添加自己锁拥有的技能
    在ConvertItemTree.py的__item_tree中添加物品对应的类别
    在skill_influent_items.config中添加技能影响的物品类别
    在技能分类的skill.config中添加技能效果
    在 run.py 文件 -> main() 函数 -> order_list 表中添加单个订单要建造的内容， 在 order_count 中设置要建造的订单数量。
    运行 run.py

Note: 
1、所有材料效率的结果都是向上取整，所有提炼的结果都是向下取整

WARNNING:
    不要随便在配置文件中添加特殊符号，如: #  //  @ 等等包括但不限于此，否则会导致配置文件解析失败
    空格缩进一定要按规则来，否则会导致配置文件解析失败

Next Work:
    完善其余舰船配置
    添加额外的效率配置（如，军团堡垒加成，解码器加成）