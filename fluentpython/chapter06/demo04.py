'''
找出模块中的全部策略
'''
from abc import ABC, abstractmethod
from collections import namedtuple

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


def fidelity_promo(order):
    return order.total() * 0.05 if order.customer.fidelity >= 1000 else 0


def bulk_item_promo(order):
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * 0.1
    return discount


def large_order_promo(order):
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * 0.07
    return 0


def best_promo(order):
    promos = [globals()[name] for name in globals() if name.endswith("_promo") and name != "best_promo"]
    return max(promo(order) for promo in promos)


if __name__ == "__main__":
    print(globals())
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
