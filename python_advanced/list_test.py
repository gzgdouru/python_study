'''
列表的+, +=, 和extend的区别
'''

if __name__ == "__main__":
    testList = [1, 2, 3, 4, 5]
    print(id(testList), testList)

    testList = testList + [5, 6]
    print(id(testList), testList)

    #会报异常, 只能对列表进行+操作
    # testList = testList + (11, 12)

    testList += (7, 8)
    print(id(testList), testList)

    testList.extend((9, 10))
    print(id(testList), testList)


