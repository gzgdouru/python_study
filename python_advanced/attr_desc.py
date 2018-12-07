'''
属性描述符详解
属性描述符: 实现了__get__, __set__, __del__中任意一个
数据属性描述符: 实现了__get__和__set__
非数据属性描述符: 只实现__get__
属性查找规则:
如果user是某个类的实例，那么user.age（以及等价的getattr(user,’age’)）
首先调用__getattribute__。如果类定义了__getattr__方法，
那么在__getattribute__抛出 AttributeError 的时候就会调用到__getattr__，
而对于描述符(__get__）的调用，则是发生在__getattribute__内部的。
user = User(), 那么user.age 顺序如下：
（1）如果“age”是出现在User或其基类的__dict__中， 且age是data descriptor， 那么调用其__get__方法, 否则
（2）如果“age”出现在user的__dict__中， 那么直接返回 obj.__dict__[‘age’]， 否则
（3）如果“age”出现在User或其基类的__dict__中
（3.1）如果age是non-data descriptor，那么调用其__get__方法， 否则
（3.2）返回 __dict__[‘age’]
（4）如果User有__getattr__方法，调用__getattr__方法，否则
（5）抛出AttributeError
'''
import numbers


class Integer:
    def __init__(self, min_value=None, max_value=None):
        self._value = None
        self.min_value = min_value
        self.max_value = max_value

        if self.min_value is not None:
            if not isinstance(self.min_value, numbers.Integral):
                raise ValueError("min_value must be int")

        if self.max_value is not None:
            if not isinstance(self.min_value, numbers.Integral):
                raise ValueError("max_value must be int")

        if min_value is not None and max_value is not None:
            if min_value > max_value:
                raise ValueError("min_value must be smaller than max_value")

    def __get__(self, instance, owner):
        return self._value

    def __set__(self, instance, value):
        if not isinstance(value, numbers.Integral):
            raise ValueError("int value need")
        if self.min_value > value or self.max_value < value:
            raise ValueError("value must between min_value and max_value")
        self._value = value


class User:
    age = Integer(min_value=0, max_value=150)


if __name__ == "__main__":
    user = User()
    user.__dict__["age"] = 11
    print(user.__dict__["age"])
    print(user.age)
