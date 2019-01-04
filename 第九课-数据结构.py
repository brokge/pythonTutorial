#!/usr/bin/python

# 列表
'''
 1. 列表 当做栈使用。
 2. 列表 当做队列 使用。
 3. 列表 推导式。
 4. 嵌套列表 解析。
 5. del 语句

'''

fruits = ["apple", "orange", "apple", "orange", "bannan"]

# 元组和序列
t = 12345, 54321, 'hello!', fruits
print(t)
# 集合
'''
无序不重复的
'''
fruitsSet = {"apple", "orange", "banana", "watermillon", "pear"}

print(fruitsSet)
# 字典
'''
  1. 遍历技巧
'''
knights = {"orange": "the fruit", "dog": "the animal"}
for k, v in knights.items():
    print(k, v)


'''

 2. 排序

'''

fruits = ["apple", "orange", "apple", "orange", "bannan"]

for f in sorted(set(fruits)):
    print(f)