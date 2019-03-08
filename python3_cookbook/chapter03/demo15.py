'''
字符串转换为日期
'''
from datetime import datetime

if __name__ == "__main__":
    text = '2012-09-20'
    y = datetime.strptime(text, '%Y-%m-%d')
    z = datetime.now()
    diff = z - y
    print(diff)

    nice_z = datetime.strftime(datetime.now(), "%Y-%m-%d")
    print(nice_z)