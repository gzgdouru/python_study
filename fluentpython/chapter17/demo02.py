'''
多线程下载国旗
'''
import os
import sys
import time
from concurrent import futures

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
    if resp.status_code != 200:
        resp.raise_for_status()
    return resp.content


def show(text):
    print(text, end=" ")
    sys.stdout.flush()


def download_one(cc):
    try:
        image = get_flag(cc)
    except:
        raise
    else:
        show(cc)
        save_flag(image, cc.lower() + ".gif")
    return cc


def download_many(cc_list):
    cc_list = cc_list[:5]
    to_do = []
    with futures.ThreadPoolExecutor(max_workers=3) as executor:
        for cc in cc_list:
            future = executor.submit(download_one, cc)
            to_do.append(future)
            print("Scheduled for {}: {}".format(cc, future))

        results = []
        for future in futures.as_completed(to_do):
            try:
                res = future.result()
            except requests.HTTPError as e:
                print(f"HTTP {future}")
            print("{} result: {}".format(future, res))
            results.append(res)

    return len(results)


def main(download_many):
    t0 = time.time()
    count = download_many(POP20_CC)
    elapsed = time.time() - t0
    print("\n{} flags download in {:.2f}s".format(count, elapsed))


if __name__ == "__main__":
    main(download_many)
