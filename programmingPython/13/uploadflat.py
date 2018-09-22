import os, sys, ftplib
from mimetypes import guess_type
from getpass import getpass

nonpassive = False
remoteSite = "192.168.232.130"
remoteDir = "/usr/local/ouru/test"
remoteUser = "ouru"
#remotePass = getpass("Password for %s to %s:" % (remoteUser, remoteSite))
remotePass = "5201314ouru"
localDir = r"F:\python\HTTP"
cleanAll = True

print "connection...."
connection = ftplib.FTP(remoteSite)
connection.login(*(remoteUser, remotePass))
connection.cwd(remoteDir)
if nonpassive: connection.set_pasv(False)

if cleanAll:
    for remoteName in connection.nlst():
        try:
            print "deleting remote", remoteName
            connection.delete(remoteName)
        except:
            print "cannot delete remote", remoteName

count = 0
localFiles = os.listdir(localDir)

for localName in localFiles:
    mimType, encoding = guess_type(localName)
    mimType = mimType or "None/None"
    mainType = mimType.split("/")[0]

    localPath = os.path.join(localDir, localName)
    print "uploading", localPath, "to", localName, "as", mimType, encoding or ""

    if mimType == "text" and encoding == "None":
        locafile = open(localPath, "rb")
        connection.storlines("STOR " + localName, locafile)
    else:
        locafile = open(localPath, "rb")
        connection.storbinary("STOR " + localName, locafile)
    locafile.close()
    count += 1
connection.quit()
print "Done:", count, "file uploaded..."