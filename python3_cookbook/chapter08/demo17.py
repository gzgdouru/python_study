'''
创建不调用init方法的实例
'''
from datetime import datetime


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def today(cls):
        d = cls.__new__(cls)
        now = datetime.now()
        d.year = now.year
        d.month = now.month
        d.day = now.day
        return d

    def __str__(self):
        return f"{self.year}-{self.month}-{self.day}"


if __name__ == "__main__":
    d = Date.__new__(Date)
    data = {'year': 2012, 'month': 8, 'day': 29}
    for key, val in data.items():
        setattr(d, key, val)
    print(d)

    print(Date.today())
