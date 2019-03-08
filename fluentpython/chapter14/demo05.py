'''
生成器表达式和列表表达式的比较
'''


def gen_AB():
    print("start")
    yield "A"
    print("continue")
    yield "B"
    print("end")


if __name__ == "__main__":
    res1 = [x * 3 for x in gen_AB()]
    for i in res1:
        print(i)

    print("-"*80)

    res1 = (x * 3 for x in gen_AB())
    for i in res1:
        print(i)
