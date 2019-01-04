#!/usr/bin/python

# 字典

dict = {"name": "brokge", "age": 5, "mobile": "15158002499"}

dict["age"] = 8
dict["company"] = "小二科技"

print("dict[age]", dict["age"])
print("dict[company]", dict["company"])

del dict["name"]  # 删除键 'name'
dict.clear()  # 清空字典
del dict  # 删除字典