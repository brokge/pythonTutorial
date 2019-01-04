#!/usr/bin/python
# -*- coding: UTF-8 -*-
import re
# 打开文件
'''
正则：
(?<=name=")\w+(?=")

详细说明：
(?<=name=") 匹配以 name=" 开头

(?=") 匹配 以 " 结尾

\w+ 匹配一个以上的 字母、数字、下划线、汉字

'''


def matchAndReturn():
    fo = open('./strings.xml', "r+")
    print("文件名为", fo.name)
    keySet = set()
    
    for line in fo:
        keyStr = re.search(r'(?<=name=")\w+(?=")', line)
        if keyStr:
            keySet.add(keyStr.group()) 
            # print(keyStr.group())

    fo.close()
    return keySet


keySet = matchAndReturn()
for keyStr in keySet:
    print(keyStr)