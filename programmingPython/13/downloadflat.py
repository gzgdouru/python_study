import os, sys, ftplib
from getpass import getpass
from mimetypes import guess_type

nonpassive = False
remoteSite = "192.168.232.130"
remoteDir = "/usr/local/ouru/python/handbook"
remoteUser= "ouru"
#remotePass = getpass("password for %s on %s:" % (remoteUser, remoteSite))
remotePass = "5201314ouru"
localDir = r"F:\python\programmingPython\test"
cleanAll = True

print "connection...."
connection = ftplib.FTP(remoteSite)
connection.login(*(remoteUser, remotePass))
connection.cwd(remoteDir)
if nonpassive: connection.set_pasv(False)

if cleanAll:
    for localName in os.listdir(localDir):
        try:
            print "delete local", localName
            os.remove(os.path.join(localDir, localName))
        except:
            print "cannot delete local", localName

count = 0
remoteFiles = connection.nlst()
print "-------->", remoteFiles

for remoteName in remoteFiles:
    if remoteName in (".", ".."): continue

    mimetype, encoding = guess_type(remoteName)
    mimetype = mimetype or "None/None"
    mainType = mimetype.split("/")[0]
    localPath = os.path.join(localDir, remoteName)
    print "download", remoteName, "to", localPath, "as", mainType, encoding or ""

    if mainType == "text" and encoding == None:
        localFile = open(localPath, "w")
        callback = lambda line: localFile.write(line + "\n")
        connection.retrlines("RETR " + remoteName, callback)
    else:
        localFile = open(localPath, "wb")
        connection.retrbinary("RETR " + remoteName, localFile.write)
    localFile.close()
    count += 1

connection.quit()
print "Done:", count, "files downloaded."

