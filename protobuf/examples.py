import MsgTest
import requests

import MsgTest
import requests

def setUserLogin(msg):
    msg.mobile = "18719091650"
    msg.pwd = "22924f252015d4c967c0454e0878a89b"
    msg.app_type = 2
    msg.ostype = 2
    msg.language = 1
    msg.device_id = ""
    msg.app_factory = "anjubao"
    msg.app_area_type = 1


try:
    sendData = MsgTest.app_pb2.UserLogin()
    setUserLogin(sendData)
    msgStr = MsgTest.EncodeMsg(sendData)
    print(msgStr)

    url = "http://sap.dyajb.com:9105/sap-ajb/app/req"
    res = requests.post(url, data=msgStr)
    if res.status_code == requests.codes.ok:
        msg = MsgTest.DecodeMsg(res.content)
        print(msg)
    else:
        res.raise_for_status()
except Exception as e:
    print("Exception:", e)
