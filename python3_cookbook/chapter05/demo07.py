'''
读写压缩文件
'''
import gzip, bz2
import tarfile
import shutil

if __name__ == "__main__":
    # with tarfile.open("nginx.tar.gz") as f:
    #     f.extractall(".")

    shutil.unpack_archive("nginx.tar.gz", extract_dir=".")

    # import csv
    # import tempfile
    # f = tempfile.TemporaryFile(mode="w+")
    # writer = csv.writer(f)
    # writer.writerow(["a", "b", "c"])
    # f.seek(0)
    # print(f.read())