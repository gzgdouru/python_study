'''
创建和解压归档文件
'''
import shutil

if __name__ == "__main__":
    # shutil.make_archive("chapter12", "zip", "../chapter12")
    shutil.unpack_archive("test.tar.gz", ".")