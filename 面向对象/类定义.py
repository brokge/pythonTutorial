#!/usr/bin/python


"""
简单类定义
"""


class MyClass:
    """ 一个简单的类示例"""
    i = 123444

    def f(self):
        return "hello world"


x = MyClass()
print("MyClass 类的属性 i 为 ：", x.i)
print("MyClass 类的方法为 ：", x.f())


class Complex:
    def __init__(self, realpart, imagepart):
        self.r = realpart
        self.i = imagepart


m = Complex(3.0, 2)
print(m.r, m.i)

"""
定义属性和方法
"""


class people:
    # 定义基本属性
    name = ""
    age = 0
    # 定义私有属性 外类不能直接访问 包括继承
    __weight = 100

    def __init__(self, n, a, weight):
        self.name = n 
        self.age = a
        self. __weight = weight
    
    def speak(self):
        print(" %s 说： 我 %d 岁了,体重 %d 斤" % (self.name, self.age, self.__weight))


p = people("娇娇", 20, 120)
p.speak()

"""
继承
"""
# 单继承 


class student(people):
    grade = ''
    
    def __init__(self, n, a, w, g):
        people.__init__(self, n, a, w)
        self.grade = g
    
    # 覆写父类的方法
    def speak(self):
        print("%s 说：我 %d 岁了，我在读 %d 年级" % (self.name, self.age, self.grade))


s = student("娇娇", 12, 110, 2)
s.speak()
