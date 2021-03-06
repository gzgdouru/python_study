import os
import sys

def reportdiffs(unique1, unique2, dir1, dir2):
    if not (unique1 or unique2):
        print "directory lists are identical"
    else:
        if unique1:
            print "file unique to", dir1
            for file in unique1:
                print "......", file
        if unique2:
            print "file unique to", dir2
            for file in unique2:
                print "......", file

def difference(seq1, seq2):
    return [item for item in seq1 if item not in seq2]

def comparedirs(dir1, dir2, files1 = None, files2 = None):
    print "comparing", dir1, "to", dir2
    files1 = os.listdir(dir1) if files1 is None else files1
    files2 = os.listdir(dir2) if files2 is None else files2
    unique1 = difference(files1, files2)
    unique2 = difference(files2, files1)
    reportdiffs(unique1, unique2, dir1, dir2)
    return not (unique1 or unique2)

def getArgs():
    try:
        dir1, dir2 = sys.argv[1:]
    except:
        print "Uage: dirdiff.py dir1 dir2"
        sys.exit(1)
    else:
        return (dir1, dir2)

if __name__ == "__main__":
    dir1 = r"E:\test\ffmpeg-3.1.5-mediacodec"
    dir2 = r"F:\test\ffmpeg-3.1.5-mediacodec"
    comparedirs(dir1, dir2)