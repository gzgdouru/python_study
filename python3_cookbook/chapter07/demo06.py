'''
定义匿名或内联函数
'''

if __name__ == "__main__":
    add = lambda x, y: x + y
    print(add(2, 3))

    names = ['David Beazley', 'Brian Jones', 'Raymond Hettinger', 'Ned Batchelder']
    tmp = sorted(names, key=lambda name: name.split(" ")[-1].lower())
    print(tmp)
