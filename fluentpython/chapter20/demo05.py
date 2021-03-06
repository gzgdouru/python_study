'''
覆盖型与非覆盖型描述符对比
'''


def cls_name(obj_or_cls):
    cls = type(obj_or_cls)
    if cls is type:
        cls = obj_or_cls
    return cls.__name__.split(".")[-1]


def display(obj):
    cls = type(obj)
    if cls is type:
        return "<class {}>".format(obj.__name__)
    elif cls in [type(None), int]:
        return repr(obj)
    else:
        return "<{} object>".format(cls_name(obj))


def print_args(name, *args):
    pseudo_args = ",".join(display(x) for x in args)
    print("-> {}.__{}__({})".format(cls_name(args[0]), name, pseudo_args))


class Overriding:
    def __get__(self, instance, owner):
        print_args("get", self, instance, owner)

    def __set__(self, instance, value):
        print_args("set", self, instance, value)


class OverridingNoGet:
    def __set__(self, instance, value):
        print_args("set", self, instance, value)


class NonOverriding:
    def __get__(self, instance, owner):
        print_args("get", self, instance, owner)


class Managed:
    over = Overriding()
    over_no_get = OverridingNoGet()
    non_over = NonOverriding()

    def spam(self):
        print_args("-> Managed.spam({})".format(display(self)))


if __name__ == "__main__":
    print("-------", "覆盖型描述符", "-------")
    obj = Managed()
    obj.over
    Managed.over
    obj.over = 7
    obj.over
    obj.__dict__["over"] = 8
    print(vars(obj))
    obj.over
    print("-" * 80)

    print("-------", "没有__get__方法的覆盖型描述符", "-------")
    print(obj.over_no_get)
    print(Managed.over_no_get)
    obj.over_no_get = 7
    print(obj.over_no_get)
    obj.__dict__["over_no_get"] = 9
    print(obj.over_no_get)
    obj.over_no_get = 7
    print(obj.over_no_get)
    print("-" * 80)

    print("-------", "非覆盖型描述符", "-------")
    obj.non_over
    obj.non_over = 7
    print(obj.non_over)
    Managed.non_over
    del obj.non_over
    obj.non_over
    print("-" * 80)

    print("-------", "在类中覆盖描述符", "-------")
    Managed.over = 1
    Managed.over_no_get = 2
    Managed.non_over = 3
    print(obj.over, obj.over_no_get, obj.non_over)
    print("-" * 80)

    print("-------", "方法是描述符", "-------")
    print(obj.spam)
    print(Managed.spam)
    obj.spam = 7
    print(obj.spam)
    print("-" * 80)
