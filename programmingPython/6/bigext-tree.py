import os
import sys
import pprint

dirName = r"F:\\"
extName = ".py"
trace = 2

def tryPrint(arg):
    try:
        print arg
    except UnicodeEncodeError:
        print str(arg).encode()

visited = set()
allSize = []

for (thisDir, subsHere, filesHere) in os.walk(dirName):
    if trace: tryPrint(thisDir)
    thisDir = os.path.normpath(thisDir)
    fixName = os.path.normcase(thisDir)

    if fixName in visited:
        if trace: tryPrint("skipping" + thisDir)
    else:
        visited.add(fixName)
        for fileName in filesHere:
            if str(fileName).endswith(extName):
                if trace > 1: print "+++", fileName
                fullName = os.path.join(thisDir, fileName)
                try:
                    byteSize = os.path.getsize(fullName)
                    lineSize = sum(+1 for line in open(fullName, "rb"))
                except Exception:
                    print "error:", sys.exc_info()[0]
                else:
                    allSize.append((byteSize, lineSize, fullName))

for (title, key) in [("bytes", 0), ("lines", 1)]:
    print "\nBy %s..." % title
    allSize.sort(key=lambda x:x[key])
    pprint.pprint(allSize[:3])
    pprint.pprint(allSize[-3:])