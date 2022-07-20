#! -*- utf-8 -*-

import os
import sys

# 查看[] () {} 和表推导一起用时，返回值的类型
num1 = [i for i in range(10)]
num2 = (i for i in range(10))
num3 = {i for i in range(10)}
print('num1 type: ' + str(type(num1)))
# num1 type: <class 'list'>
print('num2 type: ' + str(type(num2)))
# num2 type: <class 'generator'>
print('num3 type: ' + str(type(num3)))
# num3 type: <class 'set'>

# 生成器的使用方法
for var in num2:
    print(var)