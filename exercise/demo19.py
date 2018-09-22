#conding:utf-8

numList = []

for i in range(1, 1001):
    total = 0
    for j in range(1, i):
        if i % j == 0:
            total += j

        if total > i: break
        if total == i :
            numList.append(total)
            break

print numList