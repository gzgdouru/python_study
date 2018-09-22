
lineNum = 1
fileStr = "../3/testIo.py"
for line in open(fileStr):
    print lineNum, ":", line,
    lineNum += 1

print
print [line for line in open("../3/testIo.py")]

print "-" * 100

str = b"\x00\xa4fge\n"
print len(str)
print open("data.bin", "w").write(str)
print open("data.bin", "rb").read()