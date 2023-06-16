import os

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]
    
class MySkill(metaclass=Singleton):
    def __init__(self):
        self.skills = {}
        self.load_skills()

    def load_skills(self):
        config_path = os.path.join(os.path.dirname(__file__), "myskill.config")
        with open(config_path, "r") as f:
            for line in f:
                key, values = line.strip().split(":")
                nums = [int(x) for x in str(int(values))]
                if nums[0] < 4:
                    if nums[1] > 0:
                        raise Exception("进阶技能大于0的时候，基础技能不能小于4")
                if nums[1] < 5:
                    if nums[2] > 0:
                        raise Exception("专家技能大于0的时候，进阶技能不能小于5")
                self.skills[key] = nums