#!/usr/bin/python

total = 0


# global
def sum(a, b):
    global total
    total = a + b
    print("局部变量 total ", total)
    return total


sum(10, 20)
print("函数外全局变量", total)


# nonlocal 修改闭包 外变量的，需要修改其作用域
def out():
    num = 10

    def inner():
        nonlocal num
        num = 100
        print(num)
    inner()
    print(num)


out()


# 默认参数，关键字参数可写函数说明
def printinfo(name, age=35):
    print("名字: ", name)
    print("年龄: ", age)
    return


# 调用printinfo函数
printinfo(age=50, name="runoob")
print("------------------------")
printinfo(name="runoob")