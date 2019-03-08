'''
找出模块中的全部策略
'''
from abc import ABC, abstractmethod
from collections import namedtuple
import inspect
import promotions

Customer = namedtuple("Customer", "name fidelity")


class LineItem:
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price * self.quantity

    def __str__(self):
        return self.product

    def __repr__(self):
        return self.product


class Order:
    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion

    def total(self):
        if not hasattr(self, "_total"):
            self._total = sum(item.total() for item in self.cart)
        return self._total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion(self)
        return self.total() - discount

    def __repr__(self):
        fmt = "<Order> total: {:.2f} due: {:.2f}"
        return fmt.format(self.total(), self.due())


promos = [func for name, func in inspect.getmembers(promotions, inspect.isfunction)]


def best_promo(order):
    '''信泽可用的最佳折扣'''
    return max(promo(order) for promo in promos)


if __name__ == "__main__":
    joe = Customer("John Doe", 0)
    ann = Customer("Ann Smith", 1100)

    cart = [
        LineItem("banana", 5, 0.5),
        LineItem("apple", 10, 1.5),
        LineItem("watermellon", 5, 5.0)
    ]
    print(Order(ann, cart, best_promo))

    banana_cart = [
        LineItem("banana", 30, 0.5),
        LineItem("apple", 10, 1.5),
    ]
    print(Order(joe, banana_cart, best_promo))

    long_order = [LineItem(str(item_code), 1, 1.0) for item_code in range(1, 11)]
    print(Order(joe, long_order, best_promo))
