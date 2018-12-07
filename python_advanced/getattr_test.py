'''
 __getattr__、__getattribute__魔法函数
 __getattr__ 就是在查找不到属性的时候调用
 __getattribute__查找属性时第一个调用
'''

class Student:
    def __init__(self, info):
        self.info = info

    # def __getattribute__(self, item):
    #     return item

    def __getattr__(self, item):
        return self.info[item]


if __name__ == "__main__":
    student = Student(info={"name":"ouru","age":26})
    print(student.name)