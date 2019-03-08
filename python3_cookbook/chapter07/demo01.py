'''
可接受任意数量参数的函数
'''
import html


def avg(first, *rest):
    return (first + sum(rest)) / (1 + len(rest))


def make_element(name, value, **attrs):
    keyvalues = [' {}="{}"'.format(item[0], item[1]) for item in attrs.items()]
    attrs_str = "".join(keyvalues)
    element = "<{name}{attrs}>{value}</{name}>".format(name=name, attrs=attrs_str, value=html.escape(value))
    return element


if __name__ == "__main__":
    # print(avg(10, 2))
    # print(avg(10, 2, 3, 4, 5))

    print(make_element('item', 'Albatross', size='large', quantity=6))
    print(make_element('p', '<spam>'))
