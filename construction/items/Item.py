class Item:
    def __init__(self, name, build_accessable=True) -> None:
        self.name = name
        self.__price = 0
        self._build_accessable = build_accessable

    def set_price(self, price) -> None:
        self.__price = price

    def get_pirce(self) -> float:
        return self.__price

    def get_build_accessabled(self) -> bool:
        return self._build_accessable

    def set_name(self, name) -> None:
        self.name = name
    
    def get_name(self):
        return self.name
    