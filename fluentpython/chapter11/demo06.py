'''
多继承和方法解析顺序
'''


class A:
    def ping(self):
        print("ping:", self)


class B(A):
    def pong(self):
        print("pong:", self)


class C(A):
    def pong(self):
        print("PONG:", self)


class D(B, C):
    def ping(self):
        super().ping()
        print("pong-ping:", self)

    def pingpong(self):
        self.ping()
        super().ping()
        self.pong()
        super().pong()
        C.pong(self)


if __name__ == "__main__":
   d = D()
   d.pingpong()