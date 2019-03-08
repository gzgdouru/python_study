'''
只接受关键字参数的函数
'''
def recv(maxsize, *, block=False):
    pass

def minimum(*values, clip=None):
    m = min(values)
    if clip is not None:
        m = clip if clip > m else m
    return m


if __name__ == "__main__":
    # recv(1024, False)
    recv(1024, block=False)

    # print(minimum(1, 5, 2, -5, 10))
    # print(minimum(1, 5, 2, -5, 10, clip=0))
