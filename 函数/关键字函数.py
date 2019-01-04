#!/usr/bin/python
'''
关键字参数 ，不需要使用指定顺序
'''


def printime(str):
    print(str)
    return


printime(str="这是个参数")


# 可写函数说明

def printinfo(name, age):
    print("名字: ", name)
    print("年龄: ",  age)
    return
 

# 调用printinfo函数
printinfo(age=50, name="runoob")