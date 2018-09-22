import struct

data = struct.pack(">i4shf", 2, "spam", 3, 1.234)
print  open("data.bin", "wb").write(data)

by2 = open("data.bin", "rb").read()
values = struct.unpack(">i4shf", by2)
print values
values[1]