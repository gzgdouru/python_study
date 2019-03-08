'''
顺序迭代合并后的排序迭代对象
'''
import heapq

if __name__ == "__main__":
    a = [1, 4, 7, 10]
    b = [2, 5, 6, 11]
    for c in heapq.merge(a, b):
        print(c, end=" ")
    print("")
