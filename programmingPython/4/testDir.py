import glob
import os

dirName = r"F:\python\programmingPython\4"

for file in glob.glob(dirName + "/*"):
    head, tail = os.path.split(file)
    print head, "=>", ("f:/other/" + tail)

print "-" * 50

for file in os.listdir(dirName):
    print dirName, file, "=>", os.path.join(dirName, file)


print "-" * 50

for (dirHere, subHere, fileHere) in os.walk(r"F:\python\programmingPython"):
    print "curDir:", dirHere
    print "subDir:", subHere
    print "file:", fileHere