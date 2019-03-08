'''
使用多个界定符分割字符串
'''
import re

if __name__ == "__main__":
    line = 'asdf fjdk; afed, fjek,asdf, foo'
    text = re.split(r'[\s;,]\s*', line)
    print(text)

    fields = re.split(r'(\s|;|,)\s*', line)
    print(fields)

    fields = re.split(r'(?:\s|;|,)\s*', line)
    print(fields)
