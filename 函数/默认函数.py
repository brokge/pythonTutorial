#!/usr/bin/python

# 可写函数说明


def printinfo(name, age=35):
    print("名字: ", name)
    print("年龄: ", age)
    return


# 调用printinfo函数
printinfo(age=50, name="runoob")
print("------------------------")
printinfo(name="runoob")
