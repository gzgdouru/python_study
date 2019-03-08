'''
在类中封装属性名
'''
class A:
    def __init__(self):
        self._internal = 0
        self.__private = 0
        self.public = 1

    def get_internal(self):
        print(self._internal)

    def get_private(self):
        print(self.__private)

    def get_public(self):
        print(self.public)


class B(A):
    def __init__(self):
        super().__init__()
        self._internal = 10
        self.__private = 11

    def get_private_2(self):
        print(self.__private)


if __name__ == "__main__":
    b = B()
    b.get_internal()
    b.get_private()
    b.get_private_2()
    print(b.__dict__)