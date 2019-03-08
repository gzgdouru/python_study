'''
读写二进制数组数据
'''
from struct import Struct

if __name__ == "__main__":
    records = [(1, 2.3, 4.5),
               (6, 7.8, 9.0),
               (12, 13.4, 56.7)]
    record_struct = Struct("<idd")

    # with open("data.bin", "wb") as f:
    #     for r in records:
    #         f.write(record_struct.pack(*r))

    # with open("data.bin", "rb") as f:
    #     chunks = iter(lambda: f.read(record_struct.size), b'')
    #     for chunk in chunks:
    #         print(record_struct.unpack(chunk))

    # with open("data.bin", "rb") as f:
    #     data = f.read()
    #     for offset in range(0, len(data), record_struct.size):
    #         print(record_struct.unpack_from(data, offset))

    print(record_struct.size)
    text = record_struct.pack(1, 2.0, 3.0)
    data = record_struct.unpack(text)
    print(data)