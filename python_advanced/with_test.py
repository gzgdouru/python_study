'''
with语句的实现
'''

import contextlib

class ParodyWith:
    def __enter__(self):
        print("start...")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("end!!!!")

    def do_something(self):
        print("do something!")


@contextlib.contextmanager
def context_test():
    print("the start...")
    yield
    print("the end!!!!")

if __name__ == "__main__":
    with ParodyWith() as p:
        p.do_something()
        raise KeyError("haha")

    # with context_test() as con:
    #     print("test...")
    #     raise KeyError("YES!")
    # print(111)