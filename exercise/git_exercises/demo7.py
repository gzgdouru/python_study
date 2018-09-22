#有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来
import os

def get_files(fileDir):
    fileList = os.listdir(fileDir)
    fileList = map(lambda file: os.path.join(fileDir, file), fileList)
    return fileList

def get_file_content(filePath):
    if not os.path.exists(filePath):
        print("%s is not exist!" % filePath)
        return None

    contentList = []
    [contentList.append(line) for line in open(filePath, "r", encoding='utf8')]
    return contentList

def stats_single_file(contentList):
    codeNum = 0
    emptyNum = 0
    noteNum = 0
    for line in contentList:
        line = line.strip()
        if not line:
            emptyNum += 1
        elif line[0] == "#":
            noteNum += 1
        else:
            codeNum += 1
    return codeNum, noteNum, emptyNum

if __name__ == "__main__":
    files = get_files(".")
    totalCodeNum = 0
    totalNoteNum = 0
    totalEmptyNum = 0
    for file in files:
        text = get_file_content(file)
        codeNum, noteNum, emptyNum = stats_single_file(text)
        totalCodeNum += codeNum
        totalNoteNum += noteNum
        totalEmptyNum += emptyNum
        # print(file, codeNum, noteNum, emptyNum)
    print("code:{0} note:{1} empty:{2}".format(totalCodeNum, totalNoteNum, totalEmptyNum))