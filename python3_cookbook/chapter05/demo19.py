'''
创建临时文件和文件夹
'''
from tempfile import TemporaryFile, NamedTemporaryFile, TemporaryDirectory
import tempfile

if __name__ == "__main__":
    # with TemporaryFile("w+") as f:
    #     f.write("hello world!\n")
    #     f.write("testing\n")
    #     f.seek(0)
    #     print(f.read())
    print(tempfile.gettempdir())

    # with NamedTemporaryFile("w") as f:
    #     print(f.name)

    with TemporaryDirectory() as dirname:
        print('dirname is:', dirname)
