import skill.GetSkillEffect as gse

def parsing_my_skill():
    data = {}
    with open("myskill.config", "r") as f:
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


def main():
    
    item_name = "渡神级"
    
    cls_gse = gse.GetSkillEffect()
    skill_names = cls_gse.get_skill_name_by_item_name(item_name)
    
    pass


if __name__ == "__main__":
    main()