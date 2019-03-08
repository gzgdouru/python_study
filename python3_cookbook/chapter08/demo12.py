'''
定义接口或者抽象基类
'''
from abc import ABCMeta, abstractmethod


class IStream(metaclass=ABCMeta):
    @abstractmethod
    def read(self, maxbytes=-1):
        pass

    @abstractmethod
    def write(self, data):
        pass


class MyStream(IStream):
    def read(self, maxbytes=-1):
        print("hahha")

    def write(self, data):
        print("sbsbsbs")


if __name__ == "__main__":
    stream = MyStream()
    stream.read()
