#!/usr/bin/python
# 算术运算符号

# 比较运算

# 赋值运算
a = 5
b = 2
c = 0
c = a+b
print("c+b=", c)
c = a-b
print("a-b=", c)
c = a*b
print("a*b=", c)
c = a/b
print("a/b=",  c)
c = a % b
print("a%b=", c)
# 幂 - 返回x的y次幂
c = a**b
print("a**b=", c)
# 取整除 - 向下取接近除数的整数
c = a // b
print("a//b=", c)


# 位运算符
a = 60  # 60= 0011 1100
b = 13  # 14= 0000 1101

print(a & b)

print(a | b)

print(a ^ b)

print(~ a)

print(a << 2)

print(a >> 2)

# 逻辑运算符
a = 0
b = 20
tag = "and 运算"
if (a and b):
    print(tag+"a 和 b 都是有值的")
else:
    print(tag+"a 和 b 至少一个是没值")
tag = "or 运算"
if (a or b):
    print(tag+"a 和 b 至少一个有值")
else:
    print(tag+"a 和 b 都没有值")
tag = "not() 运算"
if not(a and b):
    print(tag+" 其中一个 为false")
else:
    print(tag+" 两个都为 true")

# python 成员运算符

a = 10
b = 20
list = [1, 2, 3, 4, 5]
tag = "in 运算"
if (a in list):
    print(tag+"list 包含 a")
else:
    print(tag+"list 不包含 a")
tag = "not in 运算"
if (a not in list):
    print(tag+" list 不包含 a ")
else:
    print(tag+" list 包含 a")


# 身份运算符

a = "哈哈"
b = "哈哈"
tag = "is "
if(a is b):
    print(tag, id(a), id(b))
    print(tag+"a 和 b 有相同的表示")
else:
    print(tag+"a 和 b 没有相同的标识")