import json
import re
import string
import random

import requests


def generate_code():
    seeds = string.digits
    random_str = [str(random.choice(seeds)) for i in range(6)]
    return "".join(random_str)


def send_mobile_code(mobile, code):
    url = r'https://api.mysubmail.com/message/xsend'

    params = {
        "code": code,
        "time": 10,
    }

    data = {
        "appid": "27038",
        "to": mobile,
        "project": "Qtnph1",
        "vars": json.dumps(params),
        "signature": "c7ed55eb026edf67c87183a28948872a",
    }

    response = requests.post(url, data=data)
    res = json.loads(response.text)
    return res
