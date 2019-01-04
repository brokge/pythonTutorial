#!/usr/bin/python

number = 7
guess = -1
print("猜字游戏")
while guess != number:
    guess = int(input("请输入你猜的数字"))
    if guess == number:
        print("哇  你猜对了")
    elif guess < number:
        print("哇 你猜小了")
    elif guess > number:
        print("哇 你猜大了")