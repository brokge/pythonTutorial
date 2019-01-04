#!/usr/bin/python

list = []

a = 10
while a < 100:
    a = int(input("请输入一个数字"))
    list.append(a)
else:
    print("输入的 a大于100 le", a)

for aS in list:
    print("刚才输入的数字为:", aS)

for i in range(20):
    print(i)
