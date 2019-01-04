#!/usr/bin/python

while True:
    try:
        x = int(input(" 请输入 一个数字："))
    except ValueError as err:
        print("Oop ,输入的{0}不是一个数字,Try agin".format(err))
    else:
        print("您的输入是{0}", str(x))
        break

