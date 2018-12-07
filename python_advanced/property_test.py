'''
pyhon动态属性
'''
from datetime import date, datetime
import numbers


class Student:
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday
        self._age = None

    @property
    def age(self):
        self._age = date.today().year - self.birthday.year
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, numbers.Integral):
            raise ValueError("age must be int!")
        if value < 0 or value > 200:
            raise ValueError("age must between 0~200!")
        self._age = value


if __name__ == "__main__":
    student = Student(name="ouru", birthday=date(1992, 8, 15))
    student.age = 10
    print(student.age)
