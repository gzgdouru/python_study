'''
作为客户端与HTTP服务交互
'''
from urllib import parse
import requests

if __name__ == "__main__":
    # parms = {
    #     'name1': 'value1',
    #     'name2': '<ouru>'
    # }
    #
    # print(parse.urlencode(parms))

    url = 'http://httpbin.org/post'
    files = {'file': ('README.txt', open('README.txt', 'rb'))}
    response = requests.post(url, files=files)
    print(response.text)