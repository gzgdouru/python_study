'''
在类中定义多个构造器
'''
from datetime import datetime


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def today(cls):
        now = datetime.now()
        return cls(year=now.year, month=now.month, day=now.day)

    def __str__(self):
        return f"{self.year}-{self.month}-{self.day}"


if __name__ == "__main__":
    a = Date(2012, 12, 21)
    print(a)

    b = Date.today()
    print(b)
