import os
import sys

readSize = 1024

def fileJoin(fromDir, toFile):
    outPut = open(toFile, "wb")
    parts = os.listdir(fromDir)
    parts.sort()
    for file in parts:
        fullName = os.path.join(fromDir, file)
        fileObj = open(fullName, "rb")
        while True:
            fileBytes = fileObj.read(readSize)
            if not fileBytes: break
            outPut.write(fileBytes)
        fileObj.close()
    outPut.close()

if __name__ == "__main__":
    dir = r"E:\fileSplit"
    file = r"E:\boost.zip"
    fileJoin(dir, file)