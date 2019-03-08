'''
访问闭包中定义的变量
'''
import OpenSSL

def sample():
    n = 0

    def func():
        print(f"n={n}")

    def get_n():
        return n

    def set_n(value):
        nonlocal n
        n = value

    func.get_n = get_n
    func.set_n = set_n
    return func


if __name__ == "__main__":
    s = sample()
    s()

    s.set_n(10)
    s()

    print(s.get_n())
