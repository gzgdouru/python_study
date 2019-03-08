'''
改变对象的字符串显示
'''

class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Pair({0.x!r}, {0.y!r})'.format(self)

    def __str__(self):
        return '({0.x!s}, {0.y!s})'.format(self)

if __name__ == "__main__":
    pair = Pair(3, 4)
    print("pari is {}".format(pair))
