<<<<<<< HEAD
#coding:utf8
import os
import sys

#统计文件夹下的文件数 和 子目录数
class FileVisitor:
    def __init__(self, startDir = os.curdir, content = None, trace = 2):
        self.fcount = 0
        self.dcount = 0
        self.content = content
        self.trace = trace
        self.startDir = startDir

    def run(self, reset = True):
        if reset: self.reset()
        for (thisDir, subsHere, filesHere) in os.walk(self.startDir):
            self.visitDir(thisDir)
            for fileName in filesHere:
                filePath = os.path.join(thisDir, fileName)
                self.visitFile(filePath)

    def reset(self):
        self.fcount = self.dcount = 0

    def visitDir(self, dirPath):
        self.dcount += 1
        if self.trace: print "[", dirPath, "]"

    def visitFile(self, filePath):
        self.fcount += 1
        if self.trace > 1: print self.fcount, "=>", filePath

class CopyVisitor(FileVisitor):
    def __init__(self, fromDir, toDir, verbose = 2, maxFileLoad = 1000000, blkSize = 1024 * 500):
        FileVisitor.__init__(self, trace=0)
        self.fromDir = fromDir
        self.toDir = toDir
        self.verbose = verbose
        self.maxFileLoad = maxFileLoad
        self.blkSize = blkSize
        self.createDir()

    def createDir(self):
        if os.path.split(self.fromDir)[-1] != os.path.split(self.toDir)[-1]: self.toDir += (os.sep + os.path.split(self.fromDir)[-1])
        if not os.path.exists(self.toDir): os.mkdir(self.toDir)

    def copyFile(self, fileFrom, fileTo):
        if os.path.getsize(fileFrom) <= self.maxFileLoad:
            bytesFrom = open(fileFrom, "rb").read()
            open(fileTo, "wb").write(bytesFrom)
        else:
            fileFromObj = open(fileFrom, "rb")
            fileToObj = open(fileTo, "wb")
            while True:
                bytesFrom = fileFromObj.read(self.blkSize)
                if not bytesFrom: break
                fileToObj.write(bytesFrom)
            fileFromObj.close()
            fileToObj.close()

    def visitDir(self, dirPath):
        pos = str(dirPath).find(self.fromDir)
        tempPath = "" if (pos != -1 and dirPath == self.fromDir) else dirPath[pos + len(self.fromDir):]
        tempPath = self.toDir + tempPath
        if not os.path.exists(self.toDir): os.mkdir(self.toDir)
        if self.verbose: print "copying", dirPath, "to", self.toDir
        self.dcount += 1

    def visitFile(self, filePath):
        fileName = os.path.basename(filePath)
        fileTo = os.path.join(self.toDir, fileName)
        if self.verbose > 1: print "copying", filePath, "to", fileTo
        self.copyFile(filePath, fileTo)
        self.fcount += 1

class SearchVisitor(FileVisitor):
    skipExts = []
    testExts = [".txt", ".py", ".pyw", ".html", ".c", ".h"]

    def __init__(self, searchKey, trace = 2, startDir = os.curdir):
        FileVisitor.__init__(self, startDir, searchKey, trace,)
        self.scount = 0

    def reset(self):
        self.scount = 0

    def candidate(self, fileName):
        ext = os.path.splitext(fileName)[1]
        if self.testExts:
            return ext in self.testExts
        else:
            return ext not in self.skipExts

    def visitFile(self, filePath):
        FileVisitor.visitFile(self, filePath)
        if not self.candidate(filePath):
            if self.trace > 0: print "skipping", filePath
        else:
            text = open(filePath).read()
            if self.content in text:
                self.visitMatch(filePath, text)
                self.scount += 1

    def visitMatch(self, filePath, text):
        print "-->%s has %s" % (filePath, self.content)

class EditVisitor(SearchVisitor):
    editor = r""

    def visitMatch(self, filePath, text):
        os.system("%s %s" % (self.editor, filePath))

class ReplaceVisitor(SearchVisitor):
    def __init__(self, fromStr, toStr, listOnly = False, trace = 0, startDir = os.curdir):
        SearchVisitor.__init__(self, fromStr, trace, startDir=startDir)
        self.toStr = toStr
        self.listOnly = listOnly
        self.changed = []

    def visitMatch(self, filePath, text):
        self.changed.append(filePath)
        if not self.listOnly:
            fromStr, toStr = self.content, self.toStr
            text = text.replace(fromStr, toStr)
            open(filePath, "w").write(text)

class LinesByType(FileVisitor):
    srcExts = []

    def __init__(self, trace = 1, startDir = os.curdir):
        FileVisitor.__init__(self, trace = trace, startDir=startDir)
        self.srcLines = self.srcFiles = 0
        self.extSums = {ext: dict(files = 0, lines = 0) for ext in self.srcExts}

    def visitSource(self, filePath, ext):
        if self.trace > 0: print "....", os.path.basename(filePath)
        lines = len(open(filePath, "rb").readlines())
        self.srcFiles += 1
        self.srcLines += lines
        self.extSums[ext]["files"] += 1
        self.extSums[ext]["lines"] += lines

    def visitFile(self, filePath):
        FileVisitor.visitFile(self, filePath)
        for ext in self.srcExts:
            if str(filePath).endswith(ext):
                self.visitSource(filePath, ext)
                break

class PyLines(LinesByType):
    srcExts = [".py", ".pyc"]

if __name__ == "__main__":
    '''
    fileSearchVisitor = SearchVisitor("hi", 2)
    fileSearchVisitor.run()
    print "found in %d file, visited %d" % (fileSearchVisitor.scount, fileSearchVisitor.fcount)
    '''

    '''
    visitor = EditVisitor("hi")
    visitor.run()
    print "found in %d file, visited %d" % (visitor.scount, visitor.fcount)
    '''

    '''
    visitor = ReplaceVisitor("hi", "hi", False);
    visitor.run()
    print visitor.changed
    print "found in %d file, visited %d" % (visitor.scount, visitor.fcount)
    '''

    '''
    visitor = PyLines()
    visitor.run()
    print "found in %d file and %d dir" % (visitor.fcount, visitor.dcount)
    print "source files=>%d, lines=>%d" % (visitor.srcFiles, visitor.srcLines)
    print visitor.extSums
    '''

    srcDir = r"F:\DataBase"
    dstDir = r"I:"
    visitor = CopyVisitor(srcDir, dstDir)
    visitor.run(startDir=srcDir)
=======
import os
import sys

class FileVisitor:
    def __init__(self, startDir = os.curdir, content = None, trace = 2):
        self.fcount = 0
        self.dcount = 0
        self.content = content
        self.trace = trace
        self.startDir = startDir

    def run(self, reset = True):
        if reset: self.reset()
        for (thisDir, subsHere, filesHere) in os.walk(self.startDir):
            self.visitDir(thisDir)
            for fileName in filesHere:
                filePath = os.path.join(thisDir, fileName)
                self.visitFile(filePath)

    def reset(self):
        self.fcount = self.dcount = 0

    def visitDir(self, dirPath):
        self.dcount += 1
        if self.trace: print "[", dirPath, "]"

    def visitFile(self, filePath):
        self.fcount += 1
        if self.trace > 1: print self.fcount, "=>", filePath

class CopyVisitor(FileVisitor):
    def __init__(self, fromDir, toDir, verbose = 2, maxFileLoad = 1000000, blkSize = 1024 * 500):
        FileVisitor.__init__(self, trace=0)
        self.fromDir = fromDir
        self.toDir = toDir
        self.verbose = verbose
        self.maxFileLoad = maxFileLoad
        self.blkSize = blkSize
        self.createDir()

    def createDir(self):
        if os.path.split(self.fromDir)[-1] != os.path.split(self.toDir)[-1]: self.toDir += (os.sep + os.path.split(self.fromDir)[-1])
        if not os.path.exists(self.toDir): os.mkdir(self.toDir)

    def copyFile(self, fileFrom, fileTo):
        if os.path.getsize(fileFrom) <= self.maxFileLoad:
            bytesFrom = open(fileFrom, "rb").read()
            open(fileTo, "wb").write(bytesFrom)
        else:
            fileFromObj = open(fileFrom, "rb")
            fileToObj = open(fileTo, "wb")
            while True:
                bytesFrom = fileFromObj.read(self.blkSize)
                if not bytesFrom: break
                fileToObj.write(bytesFrom)
            fileFromObj.close()
            fileToObj.close()

    def visitDir(self, dirPath):
        pos = str(dirPath).find(self.fromDir)
        tempPath = "" if (pos != -1 and dirPath == self.fromDir) else dirPath[pos + len(self.fromDir):]
        tempPath = self.toDir + tempPath
        if not os.path.exists(self.toDir): os.mkdir(self.toDir)
        if self.verbose: print "copying", dirPath, "to", self.toDir
        self.dcount += 1

    def visitFile(self, filePath):
        fileName = os.path.basename(filePath)
        fileTo = os.path.join(self.toDir, fileName)
        if self.verbose > 1: print "copying", filePath, "to", fileTo
        self.copyFile(filePath, fileTo)
        self.fcount += 1

class SearchVisitor(FileVisitor):
    skipExts = []
    testExts = [".txt", ".py", ".pyw", ".html", ".c", ".h"]

    def __init__(self, searchKey, trace = 2, startDir = os.curdir):
        FileVisitor.__init__(self, startDir, searchKey, trace,)
        self.scount = 0

    def reset(self):
        self.scount = 0

    def candidate(self, fileName):
        ext = os.path.splitext(fileName)[1]
        if self.testExts:
            return ext in self.testExts
        else:
            return ext not in self.skipExts

    def visitFile(self, filePath):
        FileVisitor.visitFile(self, filePath)
        if not self.candidate(filePath):
            if self.trace > 0: print "skipping", filePath
        else:
            text = open(filePath).read()
            if self.content in text:
                self.visitMatch(filePath, text)
                self.scount += 1

    def visitMatch(self, filePath, text):
        print "-->%s has %s" % (filePath, self.content)

class EditVisitor(SearchVisitor):
    editor = r""

    def visitMatch(self, filePath, text):
        os.system("%s %s" % (self.editor, filePath))

class ReplaceVisitor(SearchVisitor):
    def __init__(self, fromStr, toStr, listOnly = False, trace = 0, startDir = os.curdir):
        SearchVisitor.__init__(self, fromStr, trace, startDir=startDir)
        self.toStr = toStr
        self.listOnly = listOnly
        self.changed = []

    def visitMatch(self, filePath, text):
        self.changed.append(filePath)
        if not self.listOnly:
            fromStr, toStr = self.content, self.toStr
            text = text.replace(fromStr, toStr)
            open(filePath, "w").write(text)

class LinesByType(FileVisitor):
    srcExts = []

    def __init__(self, trace = 1, startDir = os.curdir):
        FileVisitor.__init__(self, trace = trace, startDir=startDir)
        self.srcLines = self.srcFiles = 0
        self.extSums = {ext: dict(files = 0, lines = 0) for ext in self.srcExts}

    def visitSource(self, filePath, ext):
        if self.trace > 0: print "....", os.path.basename(filePath)
        lines = len(open(filePath, "rb").readlines())
        self.srcFiles += 1
        self.srcLines += lines
        self.extSums[ext]["files"] += 1
        self.extSums[ext]["lines"] += lines

    def visitFile(self, filePath):
        FileVisitor.visitFile(self, filePath)
        for ext in self.srcExts:
            if str(filePath).endswith(ext):
                self.visitSource(filePath, ext)
                break

class PyLines(LinesByType):
    srcExts = [".py", ".pyc"]

if __name__ == "__main__":
    '''
    fileSearchVisitor = SearchVisitor("hi", 2)
    fileSearchVisitor.run()
    print "found in %d file, visited %d" % (fileSearchVisitor.scount, fileSearchVisitor.fcount)
    '''

    '''
    visitor = EditVisitor("hi")
    visitor.run()
    print "found in %d file, visited %d" % (visitor.scount, visitor.fcount)
    '''

    '''
    visitor = ReplaceVisitor("hi", "hi", False);
    visitor.run()
    print visitor.changed
    print "found in %d file, visited %d" % (visitor.scount, visitor.fcount)
    '''

    '''
    visitor = PyLines()
    visitor.run()
    print "found in %d file and %d dir" % (visitor.fcount, visitor.dcount)
    print "source files=>%d, lines=>%d" % (visitor.srcFiles, visitor.srcLines)
    print visitor.extSums
    '''

    srcDir = r"F:\DataBase"
    dstDir = r"I:"
    visitor = CopyVisitor(srcDir, dstDir)
    visitor.run(startDir=srcDir)
>>>>>>> 31b751da9cab8c64478d0c061b88c453fb75d14a
    print "found in %d file and %d dir" % (visitor.fcount, visitor.dcount)