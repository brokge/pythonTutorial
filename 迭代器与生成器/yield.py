#!/usr/bin/python
# _*_ coding: UTF-8 _*_


"""
:跟普通函数不同的是，生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个迭代器。

在调用生成器运行的过程中，每次遇到 yield 时函数会暂停并保存当前所有的运行信息，返回 yield 的值, 并在下一次执行 next() 方法时从当前位置继续运行。

调用一个生成器函数，返回的是一个迭代器对象。

"""
def h():
    print("wen chuan")
    m = yield 5
    print(m)
    d = yield 12 
    print("we are together.")

c = h()

m = c.next()

d = c.send("fighting")

try:
  c.next()
except StopIteration:
    print("we will never forget the date", m, ".", d)

