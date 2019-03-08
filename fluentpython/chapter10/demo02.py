'''
切片的原理
'''

class Myseq:
    def __getitem__(self, index):
        return index

if __name__ == "__main__":
    s = Myseq()
    print(s[1])
    print(s[1:4])
    print(s[1:4:2])
    print(s[1:4:2, 9])
    print(s[1:4:2, 7:9])

    print(slice(None, 10, 2).indices(5))
    print(slice(-3, None, None).indices(5))