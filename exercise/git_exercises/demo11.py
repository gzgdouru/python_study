# 敏感词文本文件 filtered_words.txt，里面的内容为以下内容，当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights

def get_filtered_words():
    return open("filtered_words.txt", "r", encoding="utf8").read()

def is_warning_word(word, filteredWords):
    return (filteredWords.find(word) != -1)

if __name__ == "__main__":
    filteredWords = get_filtered_words()
    word = input("enter a word: ")
    while word:
        if is_warning_word(word, filteredWords):
            print("Human Rights!")
        else:
            print("Freedom")
        word = input("enter a word: ")