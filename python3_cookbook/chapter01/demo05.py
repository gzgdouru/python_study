'''
实现一个优先级队列
'''
import heapq


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self.index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self.index, item))
        self.index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


if __name__ == "__main__":
    pq = PriorityQueue()
    pq.push("hello", 1)
    pq.push("hi", 3)
    pq.push("sb", 2)
    pq.push(3, 3)

    print(pq.pop())
    print(pq.pop())
    print(pq.pop())


    # nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
    # heapq.heapify(nums)
    # print(heapq.heappop(nums))
    # print(heapq.heappop(nums))
