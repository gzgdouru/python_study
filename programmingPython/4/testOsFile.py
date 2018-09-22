import os

fdFile = os.open("spam.txt", os.O_RDWR | os.O_BINARY | os.O_CREAT)
print os.write(fdFile, "hello stdio file\n")
print os.write(fdFile, b"hello descriptor file\n")
os.close(fdFile)

fdFile = os.open("spam.txt", os.O_RDWR | os.O_BINARY | os.O_CREAT)
content =  os.read(fdFile, 100)
print len(content)
print content

os.lseek(fdFile, 17, 0)
text = os.read(fdFile, 1)
print text

print "-" * 50

fdFile = os.open("spam.txt", os.O_RDWR | os.O_BINARY | os.O_CREAT)
objFile = os.fdopen(fdFile)
print objFile.read()
objFile.close()


