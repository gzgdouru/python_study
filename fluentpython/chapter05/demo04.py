'''
获取关于参数的信息
'''


def clip(text: str, max_len: 'int > 0' = 80) -> str:
    '''在指定长度附近截断字符串'''
    end = None

    if len(text) > max_len:
        space_before = text.rfind(' ', 0, max_len)
        if space_before >= 0:
            end = space_before
        else:
            space_after = text.rfind(' ', max_len)
            if space_after >= 0:
                end = space_after

    if end is None:
        end = len(text)
    return text[:end].strip()


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
    from inspect import signature

    print(clip.__defaults__)
    print(clip.__code__.co_varnames)
    print(clip.__code__.co_argcount)
    print(clip.__annotations__)

    # sig = signature(clip)
    # print(sig)
    # for name, param in sig.parameters.items():
    #     print(param.kind, ":", name, "=", param.default)
    #     print(param.annotation)


    # sig = signature(tag)
    # my_tag = {"name": "img", "title": "Sunset Boulevard", "src": "sunset.jpg", "cls": "frame"}
    # bound_args = sig.bind(**my_tag)
    # for name, value in bound_args.arguments.items():
    #     print(name, '=', value)
    #
    # del my_tag["name"]
    # bound_args = sig.bind(**my_tag)
