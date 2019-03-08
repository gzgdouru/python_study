'''
下载osconfeed.json文件
'''
import os
import json
import warnings

import requests


def load():
    url = r'https://www.oreilly.com/pub/sc/osconfeed'
    json_path = "osconfeed.json"

    if not os.path.exists(json_path):
        msg = "downloading {} to {}".format(url, json_path)
        warnings.warn(msg)

        with open(json_path, "wb") as f:
            res = requests.get(url)
            f.write(res.text)

    with open(json_path, encoding="utf-8") as f:
        return json.load(f)


if __name__ == "__main__":
    feed = load()
    print(feed["Schedule"].keys())
    for key, value in feed["Schedule"].items():
        print("{:3} {}".format(len(value), key))
