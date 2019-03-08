'''
反向迭代
'''

class CountDown:
    def __init__(self, start):
        self._start = start

    def __iter__(self):
        n = self._start
        while n:
            yield n
            n -= 1

    def __reversed__(self):
        n = 1
        while n <= self._start:
            yield n
            n += 1

if __name__ == "__main__":
    a = [1, 2, 3, 4]
    for i in reversed(a):
        print(i, end=" ")
    print("")

    for i in CountDown(30):
        print(i, end=" ")
    print("")

    for i in reversed(CountDown(30)):
        print(i, end=" ")
    print("")