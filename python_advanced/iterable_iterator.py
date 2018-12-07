'''
可迭代对象和迭代器
可迭代对象: 实现了__iter__
迭代器: 实现了__iter__和__next
'''


class Company:
    def __init__(self, name, employee_list):
        self.name = name
        self.employee_list = employee_list

    def __getitem__(self, item):
        print("__getitem__")
        return self.employee_list[item]

    def __iter__(self):
        print("__iter__")
        # return iter(self.employee_list)
        return CompanyIterator(self.name, self.employee_list)


from collections import abc


class CompanyIterator(abc.Iterator):
    def __init__(self, name, employee_list):
        self.name = name
        self.employee_list = employee_list
        self.index = 0

    def __next__(self):
        try:
            value = (self.name, self.employee_list[self.index])
        except:
            raise StopIteration
        self.index += 1
        return value


if __name__ == "__main__":
    company = Company("catt", ["ouru", "wancaiji", "panqing"])
    for employee in company:
        print(employee)
