import os, ftpTools, sys

ftp = ftpTools.FtpTools()
ftp.configTransfer()
print ftp.remoteDir

lines = []
ftp.connection.dir()
ftp.connection.cwd("curl-7.55.1/lib/vauth")
print "------>", ftp.connection.dir(),
ftp.connection.nlst()


str = "https://pan.baidu.com/s/1gfKklnd"
passwd = "4fju"