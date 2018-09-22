# -*- coding: utf-8 -*_
import os

def lister(root):
    for (curDir, subDir, fileShere) in  os.walk(root):
        print "[" + curDir + "]"
        for file in fileShere:
            print os.path.join(curDir, file)

def mylister(root):
    print "[" + root + "]"
    for file in os.listdir(root):
        path = os.path.join(root, file)
        if not os.path.isdir(path):
            print path
        else:
            mylister(path)

if __name__ == "__main__":
    rootDir = r"F:\python\programmingPython"
    #lister(rootDir)
    mylister(rootDir)
    str = u"\xc4\xe8"
    print len(str), str
    str = "傻逼"
    print len(str), str