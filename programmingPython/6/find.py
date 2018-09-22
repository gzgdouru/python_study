import fnmatch
import os

def find(pattern, startDir = os.curdir):
    for (thisDir, subsHere, filesHere) in os.walk(startDir):
        for name in subsHere + filesHere:
            if fnmatch.fnmatch(name, pattern):
                fullPath = os.path.join(thisDir, name)
                yield fullPath

def findList(pattern, startDir = os.curdir, doSort = False):
    matches = list(find(pattern, startDir))
    if doSort:matches.sort()
    return matches

if __name__ == "__main__":
    for name in find("dec", r"F:\test\ffmpeg-3.1.5-mediacodec"):
        print name