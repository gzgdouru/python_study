'''
深入分析iter函数
'''
import random

def d6():
    return random.randint(1, 6)

if __name__ == "__main__":
    for roll in iter(d6, 1):
        print(roll)