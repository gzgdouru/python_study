import os
import sys

maxFileLoad = 1000000
blkSize = 1024 * 500

def copyFile(fileFrom, fileTo, maxFileLoad = maxFileLoad):
    if os.path.getsize(fileFrom) <= maxFileLoad:
        bytesFrom = open(fileFrom, "rb").read()
        open(fileTo, "wb").write(bytesFrom)
    else:
        fileFromObj = open(fileFrom, "rb")
        fileToObj = open(fileTo, "wb")
        while True:
            bytesFrom = fileFromObj.read(blkSize)
            if not bytesFrom: break
            fileToObj.write(bytesFrom)
        fileFromObj.close()
        fileToObj.close()

def copyTree(dirFrom, dirTo, verbose = 0):
    if os.path.split(dirFrom)[-1] != os.path.split(dirTo)[-1]: dirTo += (os.sep + os.path.split(dirFrom)[-1])
    if not os.path.exists(dirTo): os.mkdir(dirTo)
    fcount = dcount = 0

    for fileName in os.listdir(dirFrom):
        fileFrom = os.path.join(dirFrom, fileName)
        fileTo = os.path.join(dirTo, fileName)
        if os.path.isfile(fileFrom):
            try:
                if verbose > 1: print "copying", fileFrom, "to", fileTo
                copyFile(fileFrom, fileTo)
                fcount += 1
            except:
                print "error copying", fileFrom, "to", fileTo, "skipped"
                print sys.exc_info()[0], sys.exc_info()[1]
        else:
            if verbose: print "copying", dirFrom, "to", dirTo
            try:
                if not os.path.exists(fileTo): os.mkdir(fileTo)
                below = copyTree(fileFrom, fileTo)
                fcount += below[0]
                dcount += below[1]
                dcount += 1
            except:
                print "error copying", fileFrom, "to", fileTo, "skipped"
                print sys.exc_info()[0], sys.exc_info()[1]
    return (fcount, dcount)

def copyTree2(dirFrom, dirTo, verbose = 0):
    if os.path.split(dirFrom)[-1] != os.path.split(dirTo)[-1]: dirTo += (os.sep + os.path.split(dirFrom)[-1])
    if not os.path.exists(dirTo): os.mkdir(dirTo)
    fcount = dcount = 0

    for (thisDir, subsHere, filesHere) in os.walk(dirFrom):
        pos = str(thisDir).find(dirFrom)
        tempPath = "" if (pos != -1 and thisDir == dirFrom) else thisDir[pos + len(dirFrom):]
        dirPath = dirTo + tempPath
        if not os.path.exists(dirPath): os.mkdir(dirPath)
        if verbose: print "copying", thisDir, "to", dirPath
        dcount += 1

        for fileName in filesHere:
            fileFrom = os.path.join(thisDir, fileName)
            fileTo = os.path.join(dirPath, fileName)
            try:
                if verbose > 1: print "copying", fileFrom, "to", fileTo
                copyFile(fileFrom, fileTo)
                fcount += 1
            except:
                print "error copying", fileFrom, "to", fileTo, "skipped"
                print sys.exc_info()[0], sys.exc_info()[1]
    return fcount,dcount

if __name__ == "__main__":
    dirFrom = r"F:\DataBase"
    dirTo = r"I:"
    import time
    start = time.clock()
    fcount, dcount = copyTree2(dirFrom, dirTo, 2)
    print "copied", fcount, "files", dcount, "directories",
    print "in", time.clock() - start, "seconds"

