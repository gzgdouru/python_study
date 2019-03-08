'''
从定位参数到仅限关键字参数
'''


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
    print(tag("br"))
