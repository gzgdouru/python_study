'''
用Shell通配符匹配字符串
'''
from fnmatch import fnmatch, fnmatchcase

if __name__ == "__main__":
    print(fnmatch("foo.txt", "*.txt"))
    print(fnmatch('foo.txt', '?oo.txt'))
    print(fnmatch('Dat45.csv', 'Dat[0-9]*'))
    names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
    print([name for name in names if fnmatch(name, 'Dat*.csv')])


    print(fnmatch('foo.txt', '*.TXT'))
    print(fnmatchcase("foo.txt", "*.TXT"))