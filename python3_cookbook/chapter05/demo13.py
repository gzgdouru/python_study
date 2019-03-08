'''
获取文件夹中的文件列表
'''
import os
import glob
import fnmatch

if __name__ == "__main__":
    names = os.listdir(".")
    print(names)

    pyfiles = glob.glob("./*.py")
    print(pyfiles)

    pyfiles = [name for name in os.listdir(".") if fnmatch.fnmatch(name, "*.bin")]
    print(pyfiles)

    pyfiles = glob.glob('*.py')
    name_sz_date = [(name, os.path.getsize(name), os.path.getmtime(name)) for name in pyfiles]
    for name, size, mtime in name_sz_date:
        print(name, size, mtime)
    print("-" * 80)
    file_metadata = [(name, os.stat(name)) for name in pyfiles]
    for name, meta in file_metadata:
        print(name, meta.st_size, meta.st_mtime)
