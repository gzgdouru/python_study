'''
在字符串中处理html和xml
'''
import html

if __name__ == "__main__":
    s = 'Elements are written as "<tag>text</tag>".'
    print(s)

    print(html.escape(s))
    print(html.escape(s, quote=False))

    re_s = html.escape(s)
    print(html.unescape(s))