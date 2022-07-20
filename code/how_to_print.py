#! -*- utf-8 -*-

print('this is your message')
# this is your message

print('this is %s' % 'your message')
# this is your message

print('this is %s %s' % ('your', 'message'))
# this is your message

print('this is {} {}'.format('your', 'message'))
# this is your message

print('this is {0} {1}'.format('your', 'message'))
# this is your message

print('this is {1} {0}'.format('message', 'your'))
# this is your message

# 以逗号分割输出列表的值
teams = ['a', 'b']
print(','.join(teams))
# a,b

pi = 3.141592653

# 字段宽10，精度3
print('%10.3f' % pi)
#     3.142

# 从pi = 开始，宽度为15， 精度为3
print("pi = %*.*f" % (15, 3, pi))
# pi =           3.142

# 用0填充空白
print('%010.3f' % pi)
# 000003.142

# 左对齐
print('%-10.3f' % pi)
# 3.142     # 2后面有5个空格

# 显示正负号
print('%+f' % pi)
# +3.141593

# 不断行显示0~9
for x in range(0, 10):
    print (x, end = '')
print()

# 以16, 10, 6进制格式输出
nHex = 0xFF
print("nHex = %x,nDec = %d,nOct = %o" %(nHex,nHex,nHex))
# nHex = ff,nDec = 255,nOct = 377

print('this', 'is', 'your', 'message', sep='==')
# this==is==your==message

# 输出参数本体
print('%r' % 123)
# 123
print('%r' % '123')
# '123'
print('{!r}'.format(123))
# 123
print('{!r}'.format('123'))
# '123'