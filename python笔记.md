# 框架
###  dateutil 
```
from dateutil.parser import parse

parse('2018-04-29T17:45:25Z')
```
# Python 特性
- python 中一切都是对象，严格意义我们不能说值传递还是引用传递，我们应该说传不可变对象和传可变对象。
- 不可变对象： string，tuples ，numbers .可变对象 list，dict.

```
a=[1,2,3]

a="Runoob"
```
> 以上代码 `[1,2,3]` 是 List 类型，`"Runoob"` 是 String 类型，而变量 a 是没有类型，她仅仅是一个对象的引用（一个指针），可以是指向 List 类型对象，也可以是指向 String 类型对象。

