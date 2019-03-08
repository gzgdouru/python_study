'''
通过字符串调用对象方法
'''
import math
import operator


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Point({!r:},{!r:})'.format(self.x, self.y)

    def distance(self, x, y):
        return math.hypot(self.x - x, self.y - y)


if __name__ == "__main__":
    p = Point(2, 3)
    d = getattr(p, "distance")(0, 0)
    print(d)

    d = operator.methodcaller("distance", 0, 0)(p)
    print(d)

    points = [
        Point(1, 2),
        Point(3, 0),
        Point(10, -3),
        Point(-5, -7),
        Point(-1, 8),
        Point(3, 2)
    ]
    points.sort(key=operator.methodcaller("distance", 0, 0))
    print(points)
    points.sort(key=lambda p: getattr(p, "distance")(0, 0))
    print(points)
