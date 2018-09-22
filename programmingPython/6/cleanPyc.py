import os
import sys

findOnly = True
rootDir = os.getcwd() if len(sys.argv) == 1 else sys.argv[1]

found = removed = 0
for (thisDir, subsHere, filesHere) in os.walk(rootDir):
    for fileName in filesHere:
        if str(fileName).endswith(".pyc"):
            fullName = os.path.join(thisDir, fileName)
            print "=>", fullName
            if not findOnly:
                try:
                    os.remove(fullName)
                    removed += 1
                except:
                    type, inst = sys.exc_info()[:2]
                    print "*" * 4, "falied:", fileName, type, inst
            found += 1
print "Found:", found, "file, removed:", removed

import find
count = 0
for fileName in find.find("*.pyc", rootDir):
    count += 1
    print "-->", fileName
    if not findOnly: os.remove(fileName)

print "find %d .pyc file" % count