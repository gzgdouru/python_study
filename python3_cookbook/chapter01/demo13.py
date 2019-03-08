'''
通过某个关键字排序一个字典列表
'''
from operator import itemgetter

if __name__ == "__main__":
    rows = [
        {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
        {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
        {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
        {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
    ]
    rows_by_name = sorted(rows, key=itemgetter("fname"))
    print(rows_by_name)

    rows_by_uid = sorted(rows, key=itemgetter("uid"))
    print(rows_by_uid)

    rows_by_lfname = sorted(rows, key=itemgetter('lname', 'fname'))
    print(rows_by_lfname)

    min_row_by_uid = min(rows, key=itemgetter("uid"))
    print(min_row_by_uid)

    max_row_by_uid = max(rows, key=itemgetter("uid"))
    print(max_row_by_uid)
