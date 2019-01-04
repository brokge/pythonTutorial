#!/usr/bin/python

'''
 带一个 * 的是 元组不定长参数
'''


# 可写函数说明
def printinfo(arg1, *vartuple):
    print("输出: ")
    print(arg1)
    print(vartuple)


# 调用printinfo 函数
printinfo(70)
printinfo(70, 60, 50)


'''
 带2个 ** 的是 字典不定长参数

'''


# 可写函数说明
def printinfotwo(arg1, **vardict):
    print("输出: ")
    print(arg1)
    print(vardict)
 

# 调用printinfo 函数
printinfotwo(1, a=2, b=3)


def printinfo3(arg1, arg2, *, arg4):
    print("输出：")
    print(arg1)
    print(arg2)
    print(arg4)
    return 


printinfo3(1, 2, arg4=4)