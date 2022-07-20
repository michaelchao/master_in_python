#! -*- utf-8 -*-

import os
import sys

# for python3, this is NameError:name ‘xrange’ is not defined
# 替换所有xrange为range，因为在python3中，xrange和range合并了
# print([ x * 2 for x in xrange(10) ])

# 把0~9中的每个数字乘以2组成一个列表，再输出这个列表
print([ x * 2 for x in range(10) ])
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# 输出当前目录下所有是目录类型的文件
print([x for x in os.listdir('.') if os.path.isdir(x)])

# 输出当前目录下所有是文件类型且文件后缀为.py的文件
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])

# 输出下面这个列表中所有的偶数
num = [1, 2, 3, 4, 5]
even = [number for number in num if number % 2 == 0]
print(even)
# [2, 4]

# 生成一个map，键是列表的元素索引，值是列表中的值
teams = ['a', 'b']
# enumerate可以取得列表中值的索引
teams_map = {k: v for k, v in enumerate(teams)}
print(teams_map)
# {0: 'a', 1: 'b'}

# 打印1~100， 3的倍数打印Fizz， 5的倍数打印Buzz， 既是3的倍数又是5的倍数打印FizzBuzz
#for x in range(101):
#    print('Fizz'[x % 3 * 4::] + 'Buzz'[x % 5 * 4::] or x)

# 将attrs这个map中的键和值全部大写到新的map attrs_new中
attrs = {'name':'michaelma', 'gender':'male'}
attrs_new = {k.upper(): v.upper() for k, v in attrs.items()}
print(attrs_new)
# {'NAME': 'MICHAELMA', 'GENDER': 'MALE'}