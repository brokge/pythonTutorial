#!/usr/bin/python
import pickle
import pprint
# pickle 操作文件：执行 dump 和 load 对应，每个dump 需要使用 load 加载。  
data1 = {"a": [1, 2, 3.0, 4+6j], "b": ("string", u'Unicode string'), "c": None}

selfref_list = [1, 2, 3]

output = open('data.pkl', "wb")

pickle.dump(data1, output)

pickle.dump(selfref_list, output, -1)
output.close()


pkl_file = open("data.pkl", "rb")

data1 = pickle.load(pkl_file)
pprint.pprint(data1)

data2 = pickle.load(pkl_file)
pprint.pprint(data2)

pkl_file.close()


