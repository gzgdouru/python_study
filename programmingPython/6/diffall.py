import os
import sys
import dirdiff

blockSize = 1024

def intersect(seq1, seq2):
    return [item for item in seq1 if item in seq2]

def comparetrees(dir1, dir2, diffs, verbose=False):
    print "-" * 20
    names1 = os.listdir(dir1)
    names2 = os.listdir(dir2)
    if not dirdiff.comparedirs(dir1, dir2, names1, names2):
        diffs.append("unique file at %s - %s" % (dir1, dir2))

    print "comparing contents..."
    common = intersect(names1, names2)
    missed = common[:]

    for name in common:
        path1 = os.path.join(dir1, name)
        path2 = os.path.join(dir2, name)
        if os.path.isfile(path1) and os.path.isfile(path2):
            missed.remove(name)
            file1 = open(path1, "rb")
            file2 = open(path2, "rb")
            while True:
                bytes1 = file1.read(blockSize)
                bytes2 = file2.read(blockSize)
                if (not bytes1) and (not bytes2):
                    if verbose: print name, "mathes"
                    break

                if bytes1 != bytes2:
                    diffs.append("file differ at %s - %s" % (path1, path2))
                    print name, "differs"
                    break

    for name in common:
        path1 = os.path.join(dir1, name)
        path2 = os.path.join(dir2, name)
        if os.path.isdir(path1) and os.path.isdir(path2):
            missed.remove(name)
            comparetrees(path1, path2, diffs, verbose)

    for name in missed:
        diffs.append("file missed at %s-%s: %s" % (dir1, dir2, name))
        print name, "differ"

if __name__=="__main__":
    dir1 = r"E:\test\ffmpeg-3.1.5-mediacodec"
    dir2 = r"F:\test\ffmpeg-3.1.5-mediacodec"
    diffs = []
    comparetrees(dir1, dir2, diffs)
    print "=" * 40
    for diff in diffs:
        print diff