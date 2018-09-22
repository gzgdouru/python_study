import os
import glob
import sys

dirName = r"F:"

allSizes = []
allpy = glob.glob(dirName + os.sep + "*.py")
#allpy = os.listdir(dirName)
print allpy

for fileName in allpy:
    fileSize = os.path.getsize(fileName)
    allSizes.append((fileSize, fileName))

allSizes.sort()
print allSizes[:2]
print allSizes[-2:]