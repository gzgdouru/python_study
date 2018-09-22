#敏感词文本文件 filtered_words.txt，里面的内容 和 0011题一样，当用户输入敏感词语，则用 星号 * 替换，例如当用户输入「北京是个好城市」，则变成「**是个好城市]

def get_filtered_word_list():
    wordList = []
    [wordList.append(word.strip()) for word in open("filtered_words.txt", "r", encoding="utf8")]
    return wordList

def replace_warning_word(content, filterWords):
    for word in filterWords:
        content = content.replace(word, "*"*len(word))
    return content

if __name__ == "__main__":
    filterWords = get_filtered_word_list()
    content = input("enter content: ")
    while content:
        content = replace_warning_word(content, filterWords)
        print(content)
        content = input("enter content: ")
