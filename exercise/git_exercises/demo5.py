#你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小
from PIL import Image
import os, re

if __name__ == "__main__":
    fileDir = r"f:/images"
    fileList = os.listdir(fileDir)

    pattern = re.compile(r".*\.[jpg|gif|png]+$")
    for file in fileList:
        if not pattern.search(file): continue

        filePath = os.path.join(fileDir, file)
        im = Image.open(filePath)
        im.resize((1136,640))

        text = os.path.splitext(filePath)
        saveFile = "i5_" + file
        im.save(saveFile)