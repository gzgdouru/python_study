import sys
import os
import pprint

trace = True
dirName = r"F:\\"
allSizes = []

for(thisDir, subsHere, filesHere) in os.walk(dirName):
    if trace:
        print "[", thisDir, "]"

    for fileName in filesHere:
        if str(fileName).endswith(".py"):
            if trace:
                print "[", fileName, "]"

            fullName = os.path.join(thisDir, fileName)
            fullSize = os.path.getsize(fullName)
            allSizes.append((fullSize, fullName))

allSizes.sort()
pprint.pprint(allSizes[:2])
pprint.pprint(allSizes[-2:])


