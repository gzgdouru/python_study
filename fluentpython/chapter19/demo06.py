'''
LineItem类第2班版: 能验证值的特性
'''


class LineItem:
    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        if value > 0:
            self._weight = value
        else:
            raise TypeError("value must be > 0")


if __name__ == "__main__":
    walnuts = LineItem("walnuts", 1, 10)
