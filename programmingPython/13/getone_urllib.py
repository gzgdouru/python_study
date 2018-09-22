import os, getpass
import urllib
import requests

fileName = "usr/local/ouru/python/programmingPython/12/pgbouncer"
localFile = "f:\\1.txt"
#passWord = getpass.getpass("input your password")
passWord = "5201314ouru"
remoteAddr = "ftp://ouru:%s@192.168.232.130/%s;type=i" % (passWord, fileName)
print "dowmloading", remoteAddr

#urllib.urlretrieve(remoteAddr, localFile)
remoteFile = urllib.urlopen(remoteAddr)
localfile = open(fileName, "wb")
localfile.write(remoteFile.read())
localfile.close()
remoteFile.close()
