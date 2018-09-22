#数据加密
import hashlib

if __name__ == "__main__":
    #MD5
    md5 = hashlib.md5()
    md5.update("python".encode("utf-8"))
    print(md5.hexdigest())

    #sha1
    sha1 = hashlib.sha1()
    sha1.update("python".encode("utf-8"))
    print(sha1.hexdigest())

    #带key的MD5
    md5 = hashlib.md5("python".encode("utf-8"))
    md5.update("python".encode("utf-8"))
    print(md5.hexdigest())