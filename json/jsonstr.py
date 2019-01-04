#!/usr/bin/python

import json
# json 对象转字符串
data = [{'a': 1, "c": 2}]

jsona = json.dumps(data)
print(jsona)

# json 字符串转 对象
data1 = "{\"c\": 2, \"a\": 1}"

print(json.loads(data1))