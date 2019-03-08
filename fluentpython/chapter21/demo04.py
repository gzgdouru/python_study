'''
获取类定义的顺序
'''
import abc
import collections


class AutoStorage:
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
        setattr(instance, self.storage_name, value)


class Vaildated(abc.ABC, AutoStorage):
    def __set__(self, instance, value):
        value = self.validate(instance, value)
        return super().__set__(instance, value)

    @abc.abstractmethod
    def validate(self, instance, value):
        pass


class Quantity(Vaildated):
    def validate(self, instance, value):
        if value <= 0:
            raise ValueError("value must be > 0")
        return value


class NonBlank(Vaildated):
    def validate(self, instance, value):
        value = value.strip()
        if len(value) == 0:
            raise ValueError("value cannot be empty or blank")
        return value


class EntityMeta(type):
    def __prepare__(metacls, name, bases):
        return collections.OrderedDict()

    def __init__(cls, name, bases, attr_dict):
        super().__init__(name, bases, attr_dict)
        cls._field_names = []
        for key, attr in attr_dict.items():
            if isinstance(attr, Vaildated):
                type_name = type(attr).__name__
                attr.storage_name = "_{}#{}".format(type_name, key)
                cls._field_names.append(key)


class Entity(metaclass=EntityMeta):
    @classmethod
    def filed_names(cls):
        for name in cls._field_names:
            yield name


class LineItem(Entity):
    description = NonBlank()
    weight = Quantity()
    price = Quantity()

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price


if __name__ == "__main__":
    for field in LineItem.filed_names():
        print(field)
