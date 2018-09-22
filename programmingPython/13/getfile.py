from ftplib import FTP
import os, sys

def getFile(file, site, remoteDir, user, verbose = True, refetch = True):
    if os.path.exists(file) and not refetch:
        if verbose: print file, "already fetched"
    else:
        if verbose: print "downloading", file

        local = open(file, "wb")
        try:
            remote = FTP(site)
            remote.login(*user)
            remote.cwd(remoteDir)
            remote.retrbinary("RETR " + file, local.write, 1024)
            remote.quit()
        except:
            print "error:", sys.exc_info()[0]
        finally:
            local.close()
        if verbose: print "download done...."

if __name__ == "__main__":
    file = "surfboard.png"
    remoteDir = "/usr/share/zenity/clothes"
    user = ("ouru", "5201314ouru")
    site = "192.168.232.130"
    getFile(file, site, remoteDir, user)