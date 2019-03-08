'''
数字的格式化输出
'''

if __name__ == "__main__":
    x = 1234.56789
    print(format(x, ".2f"))

    print(format(x, '>10.1f'))
    print(format(x, '<10.1f'))
    print(format(x, '^10.1f'))

    print(format(x, ','))
    print(format(x, '0,.1f'))

    print(format(x, 'e'))
    print(format(x, '0.2E'))

    print('The value is {:0,.2f}'.format(x))