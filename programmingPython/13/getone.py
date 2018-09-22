import os, sys
from getpass import getpass
from ftplib import FTP

nonpassive = False
fileName = "monk.png"
dirName = "/usr/share/zenity/clothes"
siteName = "192.168.232.130"
userInfo = ("ouru", "5201314ouru")

print "connecting....."
connection = FTP(siteName)
connection.login(*userInfo)
connection.cwd(dirName)
if nonpassive: connection.set_pasv(False)

print "download...."
localFile = open(fileName, "wb")
connection.retrbinary("RETR " +  fileName, localFile.write, 1024)
connection.quit()
localFile.close()

