'''
单线程下载国旗
'''
import os
import sys
import time

import requests

POP20_CC = "CN IN US ID BR PK NG BD RU JP MX PH VN ET EG DE IR TR CD FR".split()
BASE_URL = r'http://flupy.org/data/flags'
BASE_DIR = "downloads/"


def save_flag(img, filename):
    path = os.path.join(BASE_DIR, filename)
    with open(path, "wb") as f:
        f.write(img)


def get_flag(cc):
    url = "{}/{cc}/{cc}.gif".format(BASE_URL, cc=cc.lower())
    resp = requests.get(url)
    return resp.content


def show(text):
    print(text, end=" ")
    sys.stdout.flush()


def download_many(cc_list):
    for cc in sorted(cc_list):
        img = get_flag(cc)
        show(cc)
        save_flag(img, cc.lower() + ".gif")
    return len(cc_list)


def main(download_many):
    t0 = time.time()
    count = download_many(POP20_CC)
    elapsed = time.time() - t0
    print("\n{} flags download in {:.2f}s".format(count, elapsed))


if __name__ == "__main__":
    main(download_many)
