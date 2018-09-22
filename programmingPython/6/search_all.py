import os
import sys

listOnly = False
textExts = [".py", ".pyw", ".txt", ".c", ".h"]
fcount = vcount = 0

def searcher(startDir, searchKey):
    global fcount, vcount
    for (thisDir, subsHere, filesHere) in os.walk(startDir):
        for fileName in filesHere:
            file = os.path.join(thisDir, fileName)
            visitfile(file, searchKey)

def visitfile(file, searchKey):
    global fcount, vcount
    print vcount + 1, "=>", file
    try:
        if not listOnly:
            if os.path.splitext(file)[1] not in textExts:
                print "skipping", file
            elif searchKey in open(file).read():
                raw_input("%s has %s" % (file, searchKey))
                fcount += 1
    except:
        print "failed:", file, sys.exc_info()[0]
    vcount +=1

if __name__ == "__main__":
    root = r"f:\\"
    contentKey = "hi"
    searcher(root, contentKey)
    print "found in %d file, visited %d" % (fcount, vcount)