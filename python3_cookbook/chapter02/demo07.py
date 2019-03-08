'''
最短匹配模式
'''
import re

if __name__ == "__main__":
    text = 'Computer says "no." Phone says "yes."'
    str_pat = re.compile(r'"(.*)"')
    match_obj = str_pat.findall(text)
    print(match_obj)

    str_pat = re.compile(r'"(.*?)"')
    match_obj = str_pat.findall(text)
    print(match_obj)
