from  google.protobuf import message
import app_pb2
import socket
import struct

msgType = {
    "UserLogin" : app_pb2.UserLogin()
}

'''
def asBytesString(iNum):
    tmpStr = ""
    for i in range(0, 4):
        if iNum > 255:
            iTmpNum = iNum % 256
            tmpStr += chr(iTmpNum)
        elif iNum != 0:
            tmpStr += chr(iNum)
        else:
            tmpStr += chr(0)

        iNum /= 256

    return tmpStr[::-1]
'''
def asBytesString(iNum):
    return struct.pack(">i", iNum)

def asInt32(szStr):
    total = 0
    for i in range(0, 4):
        iNum = ord(szStr[i])
        if iNum > 0:
            total += (iNum * (256 ** (3 - i)))

    return total

def CreateMessage(typeName):
    return msgType.get(typeName, None)

def EncodeMsg(msg):
    message_type = msg.DESCRIPTOR.name
    nameLen = len(message_type) + 1
    #b32 = socket.htonl(nameLen)
    b32 = (nameLen)
    #print b32
    nameLenStr = asBytesString(b32)
    #print "len : %d,str :%s" % (len(nameLenStr), nameLenStr)

    msgHeader = nameLenStr + message_type + chr(0)
    msgStr = msgHeader + msg.SerializeToString()
    #print "len : %d,str : %s" % (len(msgStr), msgStr)

    return msgStr

def DecodeMsg(msgStr):
    HeaderLen = 4
    #NameLen = socket.ntohl(asInt32(msgStr[0 : HeaderLen]))
    NameLen = (asInt32(msgStr[0 : HeaderLen]))
    #print NameLen
    typeName = msgStr[HeaderLen : HeaderLen + NameLen - 1]
    #print typeName
    MsgDataStr = msgStr[HeaderLen + NameLen :]
    msg = CreateMessage(typeName)
    msg.ParseFromString(MsgDataStr)

    return msg
