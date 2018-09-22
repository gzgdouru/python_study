# -*- coding:utf-8 -*-
'''
    判断101-200之间有多少个素数，并输出所有素数。
'''

l = []
for i in range(101, 201):
    for j in range(2, i / 2 + 1):
        if i % j == 0:
            break

    if j == i / 2: l.append(i)

print len(l), l