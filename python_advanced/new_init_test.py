'''
__new__和__init的区别
'''
class Student:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            print("new")
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        print("init")

if __name__ == "__main__":
    student = Student()
    print(id(student))
    student2= Student()
    print(id(student2))
