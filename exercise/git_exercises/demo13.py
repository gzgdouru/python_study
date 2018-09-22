#用 Python 写一个爬图片的程序，爬 http://tieba.baidu.com/p/2166231880 的日本妹子图片
import requests
from bs4 import BeautifulSoup
import os

if __name__ == "__main__":
    url = "http://tieba.baidu.com/p/2166231880"
    html = requests.get(url).text
    path = r"f:/images"

    soup = BeautifulSoup(html, "lxml")
    imgList = soup.find_all("img")
    for i, img in enumerate(imgList):
        if img["src"][-4:] == ".jpg" and img.get("bdwater"):
            r = requests.get(img.get("src"))
            file = os.path.join(path, "{0}.jpg".format(i))
            open(file, "wb").write(r.content)