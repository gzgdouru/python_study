'''
序列化Python对象
'''
import pickle

if __name__ == "__main__":
    # data = pickle.dumps("hello world!")
    # print(data)
    # print(pickle.loads(data))

    with open("somedata.bin", "wb") as f:
        pickle.dump([1, 2, 3, 4], f)
        pickle.dump('hello', f)
        pickle.dump({'Apple', 'Pear', 'Banana'}, f)

    with open("somedata.bin", "rb") as f:
        print(pickle.load(f))
        print(pickle.load(f))
        print(pickle.load(f))
