import os
import sys

kilobytes = 1024
megabytes = kilobytes * 1000
chunkSize = int(1.4 * megabytes)

def fileSplit(fromFile, toDir, chunkSize = chunkSize):
    if not os.path.exists(toDir):
        os.mkdir(toDir)
    else:
        for file in os.listdir(toDir):
            os.remove(os.path.join(toDir, file))

    partNum = 0;
    input = open(fromFile, "rb")
    while True:
        chunk = input.read(chunkSize)
        if not chunk: break
        partNum += 1
        fileName = os.path.join(toDir, ("part%04d" % partNum))
        fileObj = open(fileName, "wb")
        fileObj.write(chunk)
        fileObj.close()
    input.close()
    assert partNum <= 9999
    return partNum

if __name__ == "__main__":
    file = r"E:\test\boost_1_65_1.7z"
    dir = r"E:\fileSplit"
    print fileSplit(file, dir)

