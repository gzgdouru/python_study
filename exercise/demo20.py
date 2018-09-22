#coding:utf-8
'''
一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
'''

start = 100
total = 0
for i in range(10):
    end = start / 2.0
    total += (start + end)
    start /= 2.0

print total, end