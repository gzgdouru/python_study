#你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词
import os
import re

def get_files(fileDir):
    fileList = os.listdir(fileDir)
    fileList = map(lambda file: os.path.join(fileDir, file), fileList)
    return fileList

def get_word_list(filePath):
    if not os.path.exists(filePath):
        print("%s is not exist!" % filePath)
        return None

    if os.path.splitext(filePath)[1] != ".txt": return None

    pattern = re.compile(r"[a-zA-Z]+\b")
    wordList = pattern.findall(open(filePath).read())
    return wordList

def stats_word(words):
    if not words: return None, None
    statDict = {}
    for word in words:
        if word in statDict:
            statDict[word] += 1
        else:
            statDict[word] = 1
    statDict = {statDict[key]:key for key in statDict}
    return max(statDict), statDict[max(statDict)]

if __name__ == "__main__":
    files = get_files(r"F:\git\python\myProject\english\data_source\lessons")
    for file in files:
        words = get_word_list(file)
        times, word = stats_word(words)
        if word: print(file, word, times)