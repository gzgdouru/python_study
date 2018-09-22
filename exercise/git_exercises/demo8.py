#一个HTML文件，找出里面的正文
import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":
    url = r"https://www.cnblogs.com/nancyzhu/p/8449545.html"
    html = requests.get(url).text

    soup = BeautifulSoup(html, "lxml")
    # print(soup.prettify())

    body = soup.body

    pList = body.find_all("p")

    for p in pList:
        print(p.string)