'''
字符串开头或结尾匹配
'''

if __name__ == "__main__":
    url = 'ftp://www.python.org'
    print(url.startswith("http:"))
    print(url.endswith(".org"))

    print(url.startswith(("http:", "https:", "ftp:")))