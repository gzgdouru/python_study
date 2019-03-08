'''
特性全解析
'''


class Class:
    data = "the class data attr"

    @property
    def prop(self):
        return "the prop value"


if __name__ == "__main__":
    print("-------", "特性会覆盖实例属性", "_____")
    obj = Class()
    print(vars(obj))
    print(obj.data)
    obj.data = "bar"
    print(vars(obj))
    print(obj.data)
    print(Class.data)
    print("-" * 80)

    print("-------", "实例属性不会覆盖类特性", "_____")
    print(Class.prop)
    print(obj.prop)
    obj.__dict__["prop"] = "foo"
    print(vars(obj))
    print(obj.prop)
    Class.prop = "baz"
    print(obj.prop)
    print("-" * 80)

    print("-------", "新添的类特性遮盖现有的实例特性", "_____")
    print(obj.data)
    print(Class.data)
    Class.data = property(lambda self:'the "data" prop value')
    print(obj.data)
    del Class.data
    print(obj.data)
    print("-" * 80)