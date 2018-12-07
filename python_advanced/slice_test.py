'''
自定义对象实现序列操作
'''
import numbers


class Classes:
    def __init__(self, class_name, students):
        self.class_name = class_name
        self.students = students

    def __getitem__(self, index):
        cls = type(self)
        if isinstance(index, slice):
            return cls(self.class_name, self.students[index])
        elif isinstance(index, numbers.Integral):
            return cls(self.class_name, self.students[index])

    def __iter__(self):
        cls = type(self)
        for student in self.students:
            yield cls(self.class_name, student)

    def __contains__(self, item):
        return (item in self.students)

    def __reversed__(self):
        cls = type(self)
        cls = type(self)
        for student in reversed(self.students):
            yield cls(self.class_name, student)

    def __len__(self):
        return len(self.students)

    def __str__(self):
        return "班级:{0}, 学生:{1}".format(self.class_name, self.students)


if __name__ == "__main__":
    c = Classes(class_name="一年二班", students=["ouru", "wancaiji", "panqing", "laozhan"])
    for i in c:
        print(i)