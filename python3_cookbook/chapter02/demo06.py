'''
字符串忽略大小写的搜索替换
'''
import re


def matchcase(word):
    def replace(m):
        text = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word

    return replace


if __name__ == "__main__":
    text = 'UPPER PYTHON, lower python, Mixed Python'
    match_obj = re.findall("python", text, re.IGNORECASE)
    print(match_obj)

    re_text = re.sub("python", "snake", text, flags=re.IGNORECASE)
    print(re_text)

    re_text = re.sub("python", matchcase("snake"), text, flags=re.IGNORECASE)
    print(re_text)
