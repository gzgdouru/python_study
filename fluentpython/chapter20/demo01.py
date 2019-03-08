'''
定义一个特性工厂函数
'''


def quantity(storage_name):
    def qty_getter(instance):
        return instance.__dict__[storage_name]

    def qty_setter(instance, value):
        if value > 0:
            instance.__dict__[storage_name] = value
        else:
            raise TypeError("value must be > 0")

    return property(qty_getter, qty_setter)


class LineItem:
    weight = quantity("weight")
    price = quantity("price")

    def __init__(self, descripton, weight, price):
        self.description = descripton
        self.weight = weight
        self.price = price


if __name__ == "__main__":
    nutmeg = LineItem("Moluccan nutmeg", 8, 13.95)
    print(nutmeg.weight, nutmeg.price)
    print(vars(nutmeg).items())

    nutmeg.__dict__["weight"] = -1
    print(nutmeg.weight, nutmeg.price)
    print(vars(nutmeg).items())

