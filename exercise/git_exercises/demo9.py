#一个HTML文件，找出里面的链接
import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":
    url = "https://www.cnblogs.com/nancyzhu/p/8449545.html"
    html = requests.get(url).text

    soup = BeautifulSoup(html, "lxml")
    aList = soup.find_all("a")
    for a in aList:
        print(a)