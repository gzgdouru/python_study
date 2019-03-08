'''
保留最后 N 个元素
'''
from collections import deque

if __name__ == "__main__":
    q = deque(maxlen=3)
    q.append(1)
    q.append(2)
    q.append(3)
    print(q)

    q.append(4)
    print(q)

    q.appendleft(5)
    print(q)
