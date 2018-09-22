#coding:utf-8
'''
输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
'''

import re

lines = "hdga4da 45845dasda 454das"

iList = re.findall("[0-9]", lines)
cList = re.findall("[a-zA-Z]", lines)
sList = re.findall(" ", lines)

print len(iList), len(cList), len(sList), len(lines)