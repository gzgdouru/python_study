import sys
import os
import pprint

trace = 2
visited = {}
allSize = []

for srcDir in sys.path:
    for (thisDir, subsHere, filesHere) in os.walk(srcDir):
        if trace > 0: print "[", thisDir, "]"
        thisDir = os.path.normpath(thisDir)
        fixcase = os.path.normcase(thisDir)
        if fixcase in visited:
            continue
        else:
            visited[fixcase] = True

        for fileName in filesHere:
            if str(fileName).endswith(".py"):
                if trace > 1: print "....", fileName
                pyPath = os.path.join(thisDir, fileName)
                try:
                    pySize = os.path.getsize(pyPath)
                except os.error:
                    print "skipping", pyPath, sys.exc_info()[0]
                else:
                    pyLines = len(open(pyPath, "rb").readlines())
                    allSize.append((pySize, pyLines, pyPath))

print "By Size....."
allSize.sort()
pprint.pprint(allSize[:3])
pprint.pprint(allSize[-3:])

print "By Lines....."
allSize.sort(key=lambda x : x[1])
pprint.pprint(allSize[:3])
pprint.pprint(allSize[-3:])
