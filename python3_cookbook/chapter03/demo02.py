'''
执行精确的浮点数运算
'''
from decimal import Decimal, localcontext

if __name__ == "__main__":
    a = Decimal("4.2")
    b = Decimal("2.1")
    c = a + b
    print(c)
    print(c == Decimal("6.3"))

    a = Decimal('1.3')
    b = Decimal('1.7')
    print(a / b)

    with localcontext() as ctx:
        ctx.prec = 3
        print(a / b)
