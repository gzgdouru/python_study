'''
过滤序列元素
'''
from itertools import compress

def is_int(val):
    try:
        x = int(val)
        return True
    except:
        return False

if __name__ == "__main__":
    values = ['1', '2', '-3', '-', '4', 'N/A', '5']
    print([value for value in values if is_int(value)])
    print(list(filter(is_int, values)))

    addresses = [
        '5412 N CLARK',
        '5148 N CLARK',
        '5800 E 58TH',
        '2122 N CLARK',
        '5645 N RAVENSWOOD',
        '1060 W ADDISON',
        '4801 N BROADWAY',
        '1039 W GRANVILLE',
    ]
    counts = [0, 3, 10, 4, 1, 7, 6, 1]
    more5 = [num > 5 for num in counts]
    print(more5)
    print(list(compress(addresses, more5)))
    print([value[0] for value in zip(addresses, counts) if value[1] > 5])
