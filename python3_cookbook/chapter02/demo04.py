'''
字符串匹配和搜索
'''
import re

if __name__ == "__main__":
    text1 = '11/27/2012'
    text2 = 'Nov 27, 2012'

    datepat = re.compile(r'\d+/\d+/\d+')
    if datepat.match(text1):
        print("match text1")

    if datepat.match(text2):
        print("match text2")

    text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
    datepat = re.compile(r'(\d+)/(\d+)/(\d+)')

    match_obj = datepat.match(text1)
    print(match_obj.group())
    print(match_obj.groups())

    match_obj = datepat.findall(text)
    print(match_obj)

    matchs = datepat.finditer(text)
    for match_obj in matchs:
        print(match_obj.group())

    match_obj = re.findall(r'(\d+)/(\d+)/(\d+)', text)
    print(match_obj)