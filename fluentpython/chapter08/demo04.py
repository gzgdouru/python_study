'''
弱引用
'''
import weakref

if __name__ == "__main__":
    a_set = {0, 1}
    wref = weakref.ref(a_set)
    print(wref)
    print(wref())

    a_set = {2, 3, 4}
    print(wref())