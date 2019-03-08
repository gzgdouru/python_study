'''
定义__getitem__方法, 只实现序列协议的一部分, 这样就足够访问元素, 迭代和使用in运算符
'''
class Foo:
    def __getitem__(self, index):
        return range(0, 30, 10)[index]

if __name__ == "__main__":
    f = Foo()
    print(f[1])

    for i in f:
        print(i, end=" ")
    print("")

    print(10 in f)
    print(5 in f)