'''
元类详解
元类: 元类是创建类的类
'''


class MetaClass(type):
    def __new__(cls, class_name, class_parents, class_attr, **kwargs):
        new_class_attr = {}
        for key, value in class_attr.items():
            if not key.startswith('__'):
                new_class_attr[key.upper()] = value
            else:
                new_class_attr[key] = value
        return super().__new__(cls, class_name, class_parents, new_class_attr, **kwargs)


# python中类的实例化过程，会首先寻找metaclass，通过metaclass去创建user类
class User():
    name = "ouru"

    def __new__(cls, *args, **kwargs):
        cls.NAME = cls.name
        del cls.name
        return super().__new__(cls)

    def __init__(self, age=0):
        print("创建完毕!!!")

    def __str__(self):
        return "user"

    class Meta:
        db_table = "halo"


if __name__ == "__main__":
    user = User()
    print(dir(user))
