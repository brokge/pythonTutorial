#!/usr/bin/python

import time
from dateutil.parser import parse
print(parse('2018-04-29T17:45:25Z'))
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))