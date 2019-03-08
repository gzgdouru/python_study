'''
使用functools.partial冻结参数
'''
from operator import mul
from functools import partial


def tag(name, *content, cls=None, **attrs):
    if cls is not None:
        attrs["class"] = cls

    if attrs:
        attr_str = "".join(' %s=%s' % (attr, value) for attr, value in sorted(attrs.items()))
    else:
        attr_str = ""

    if content:
        return "\n".join("<{}{}>{}</{}>".format((name, attr_str, c, name) for c in content))
    else:
        return "<{}{} />".format(name, attr_str)


if __name__ == "__main__":
    # triple = partial(mul, 3)
    # print(triple(7))
    # print(list(map(triple, range(1, 11))))

    picture = partial(tag, "img", cls="pic-frame")
    print(picture(src="wumpus.jpg"))
    print(picture)
    print(picture.func)
    print(picture.args)
    print(picture.keywords)
