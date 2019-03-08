'''
随机选择
'''
import random

if __name__ == "__main__":
    values = [1, 2, 3, 4, 5, 6]
    print(random.choice(values))

    print(random.sample(values, 2))

    print(values)
    random.shuffle(values)
    print(values)

    print(random.randint(0, 10))

    print(random.random())

    print(random.getrandbits(200))