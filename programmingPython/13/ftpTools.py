import os, sys, ftplib
from getpass import getpass
from mimetypes import guess_type, add_type

defaultSite = "192.168.232.130"
defaultDir = "/home/ouru/pytest/ftp"
defaultUser = "ouru"

class FtpTools:
    def getLocalDir(self):
        return (len(sys.argv) > 2 and sys.argv[2]) or "."

    def getCleanAll(self):
        return (len(sys.argv) > 3 and sys.argv[3] == "false") or True
        #return raw_input("clean target dir first?")[:1] in ["y", "Y"]

    def getPassword(self):
        return getpass("Password for %s on %s:" % (self.remoteUser, self.remoteSite))

    def configTransfer(self, site = defaultSite, rDir = defaultDir, user = defaultUser):
        self.nonpassive = False
        self.remoteSite = site
        self.remoteDir = rDir
        self.remoteUser = user
        self.localDir = self.getLocalDir()
        self.cleanAll = self.getCleanAll()
        #self.remotePass = self.getPassword()
        self.remotePass = "5201314ouru"
        self.fcount = 0
        self.dcount = 0
        self.dfcount = 0
        self.ddcount = 0
        self.connecFTP()

    def isTextKind(self, remoteNamem, trace = True):
        '''
        f.html=>("text/html", None)
        f.jpeg=>("image/jpeg", None)
        f.txt.gz=>("text/plain", "gzip")
        '''
        add_type("text/x-python-win", ".pyw")
        mimType, encoding = guess_type(remoteNamem, strict=False)
        mimType = mimType or "None/None"
        mainType = mimType.split("/")[0]
        if trace: print mainType, encoding or ""
        return mainType == "text" and encoding == None

    def createPreDir(self, mode = "download"):
        remotePreDir = os.path.split(self.remoteDir)[-1]
        localPreDir = os.path.split(self.localDir)[-1]
        if remotePreDir != localPreDir:
            if mode == "upload":
                if localPreDir not in self.connection.nlst():
                    self.connection.mkd(localPreDir)
                self.connection.cwd(localPreDir)
                self.remoteDir += (os.sep + localPreDir)
            elif mode == "download":
                if remotePreDir not in os.listdir(self.localDir):
                    localFullPath = self.localDir + os.sep + remotePreDir
                    os.mkdir(localFullPath)
                    self.localDir = localFullPath

    def cleanRemoteTree(self):
        lines = []
        self.connection.dir(lines.append)
        for line in lines:
            parsed = line.split()
            permiss = parsed[0]
            fName = parsed[-1]
            if fName in (".", ".."):
                continue
            elif permiss[0] != "d":
                print "delete file:", fName
                self.connection.delete(fName)
                self.dfcount += 1
            else:
                print "directory:[", self.connection.pwd() + os.sep + fName, "]"
                self.connection.cwd(fName)
                self.cleanRemoteTree()
                self.connection.cwd("..")
                self.connection.rmd(fName)
                self.ddcount += 1

    def connecFTP(self):
        print "connection...."
        connection = ftplib.FTP(self.remoteSite)
        connection.login(*(self.remoteUser, self.remotePass))
        connection.cwd(self.remoteDir)
        if self.nonpassive: connection.set_pasv(False)
        self.connection = connection

    def cleanLocalFiles(self):
        if self.cleanAll:
            for localName in os.listdir(self.localDir):
                try:
                    print "delete local", localName
                    os.remove(os.path.join(self.localDir, localName))
                except:
                    print "cannot delete local", localName

    def cleanRemoteFiles(self):
        if self.cleanAll:
            for remoteName in self.connection.nlst():
                try:
                    print "delete remote", remoteName
                    self.connection.delete(remoteName)
                except:
                    print "cannot delete remote", remoteName

    def downloadOne(self, remoteName, localPath):
        if self.isTextKind(remoteName, False):
            localFile = open(localPath, "w")
            self.connection.retrbinary("RETR " + remoteName, lambda line: localFile.write(line + "\n"))
        else:
            localFile = open(localPath, "wb")
            self.connection.retrbinary("RETR " + remoteName, localFile.write)
        localFile.close()
        print "downloading", remoteName, "to", localPath

    def uploadOne(self, localName, localPath, remoteName):
        if self.isTextKind(localName, False):
            localFile = open(localPath, "rb")
            self.connection.storlines("STOR " + remoteName, localFile)
        else:
            localFile = open(localPath, "rb")
            self.connection.storbinary("STOR " + remoteName, localFile)
        localFile.close()
        print "uploading", localPath, "to", self.remoteDir + os.sep + remoteName

    def downloadDir(self):
        remoteFiles = self.connection.nlst()
        for remoteFile in remoteFiles:
            if remoteFile in (".", ".."): continue
            self.downloadOne(remoteFile, os.path.join(self.localDir, remoteFile))
        print "Done:", len(remoteFiles), "files downloaded.."

    def uploadDir(self):
        localFiles = os.listdir(self.localDir)
        for remoteFile in localFiles:
            localPath = os.path.join(self.localDir, remoteFile)
            self.uploadOne(remoteFile, localPath, remoteFile)
        print "Done:", len(localFiles), "files uploaded.."

    def uploadTree(self, localDir):
        localFiles = os.listdir(localDir)
        for localName in localFiles:
            localPath = os.path.join(localDir, localName)
            print "uploading", localPath, "to", localName,

            if os.path.isfile(localPath):
                self.uploadOne(localName, localPath, localName)
                self.fcount += 1
            else:
                try:
                    self.connection.mkd(localName)
                    print "create dir:[", localName, "]"
                except:
                    print "dir [", localName, "] already exist..."

                self.connection.cwd(localName)
                self.uploadTree(localPath)
                self.connection.cwd("..")
                self.dcount += 1

    def run(self, mode = "download", fileMode = "dir"):
        #self.configTransfer()
        if mode == "download":
            self.cleanLocalFiles()
            self.downloadDir()
        elif mode == "upload":
            if fileMode == "dir":
                self.cleanRemoteFiles()
                self.uploadDir()
            elif fileMode == "tree":
                self.createPreDir(mode)
                if self.cleanAll:
                    self.cleanRemoteTree()
                    print "Delete Done:", self.dfcount, "files and", self.ddcount, "directories delete..."
                self.uploadTree(self.localDir)
                print "Done:", self.fcount, "files and", self.dcount, "directories uploaded..."
        else:
            print "Usage: ftpTools.py [download | upload] [localdir] [false | true]"

        self.connection.quit()

if __name__ == "__main__":
    ftp = FtpTools()
    xferMode = sys.argv[1] if len(sys.argv) > 1 else "download"
    ftp.configTransfer()
    ftp.run(mode=xferMode, fileMode="tree")
