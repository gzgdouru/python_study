'''
单例模式实现
'''


class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


class SingletonMeta(type):
    def __init__(self, *args, **kwargs):
        # print("SingletonMeta init")
        self.__instance = None
        super().__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        # print("SingletonMeta call")
        if self.__instance is None:
            self.__instance = super().__call__(*args, **kwargs)
        return self.__instance


# class Student(Singleton):
#     __isInit = False
#
#     def __init__(self, name, age):
#         cls = type(self)
#         if not cls.__isInit:
#             cls.__isInit = True
#             self.name = name
#             self.age = age
#
#     def __str__(self):
#         return "name:{name}, age:{age}".format(name=self.name, age=self.age)

class Student(metaclass=SingletonMeta):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "name:{name}, age:{age}".format(name=self.name, age=self.age)


if __name__ == "__main__":
    s = Student("ouru", 26)
    print(s)
    s2 = Student("wancaiji", 31)
    print(s2)
    print(s)
