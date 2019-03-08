'''
字符串搜索和替换
'''
import re

if __name__ == "__main__":
    text = 'yeah, but no, but yeah, but no, but yeah'
    re_text = text.replace("yeah", "yep")
    print(re_text)

    text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
    datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
    re_text = datepat.sub(r'\3-\2-\1', text)
    print(re_text)

    re_text, n = datepat.subn(r'\3-\2-\1', text)
    print(re_text, n)