import ftplib

def putFile(file, site, dir, user, verbose=True):
    if verbose: print "uploading", file
    local = open(file, "rb")
    remote = ftplib.FTP(site)
    remote.login(*user)
    remote.cwd(dir)
    remote.storbinary("STOR " + file, local, 1024)
    remote.quit()
    local.close()
    if verbose: print "upload done..."

if __name__ == "__main__":
    site = "192.168.232.130"
    dir = "/usr/local/ouru/python/programmingPython/13"
    user = ("ouru", "5201314ouru")
    file = "surfboard.png"
    putFile(file, site, dir, user)