import Consume

class FlagshipClassIndustoryShipConsume(Consume):
    __instance = None

    def __new__(cls):
        if cls.__instance == None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    @classmethod
    def getInstance(cls):
        return cls()
    
    def __init__(self):
        super().__init__("flagship_class_industory_ship")
    
    def parsing(self):
        super().parsing()