'''
使用其他分隔符或行终止符打印
'''

if __name__ == "__main__":
    print('ACME', 50, 91.5)
    print('ACME', 50, 91.5, sep=",")
    print('ACME', 50, 91.5, end="||\n")