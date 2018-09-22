#conding:utf-8

'''
求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
'''

count = 5
num = 2
numList = []

for i in range(1, count + 1):
    numList.append(int(str(num) * i))

print numList

sum = reduce(lambda x, y: x + y, numList)
print sum