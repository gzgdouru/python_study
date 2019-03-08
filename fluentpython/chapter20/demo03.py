'''
自动获取存储属性的名称
'''


class Quantity:
    _counter = 0

    def __init__(self):
        cls = self.__class__
        prefix = cls.__name__
        index = cls._counter
        self.storage_name = "_{}#{}".format(prefix, index)
        cls._counter += 1

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return getattr(instance, self.storage_name)

    def __set__(self, instance, value):
        if value > 0:
            setattr(instance, self.storage_name, value)
        else:
            raise ValueError("value must be > 0")


class LineItem:
    weight = Quantity()
    price = Quantity()

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price


if __name__ == "__main__":
    truffle = LineItem("White truffy", 100, 1.34)
    print(truffle.subtotal())
    print(truffle.weight, truffle.price)
    print(vars(truffle))

    truffle.__dict__["weight"] = -1
    print(truffle.weight, truffle.price)
    print(vars(truffle))

    print(LineItem.price)
