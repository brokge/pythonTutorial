#!/usr/bin/python

import sys

list = [1, 2, 3, 4]

it = iter(list)
"""
for x in it:
    print(x, end=" ")
"""

while True:
    try:
        print(next(it))
    except StopIteration as s:
        print(s.message)
        sys.exit()
