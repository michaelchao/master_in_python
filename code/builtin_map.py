#! -*- utf-8 -*-

data = {'user':1, 'name':'ma'}

# 尝试获取键name对应的值，如果没有，返回False
have_name = data.get('name', False)
print(have_name)
# ma

# 尝试获取键admin对应的值，如果没有，返回False
have_admin = data.get('admin', False)
print(have_admin)
# False

my_dict = {'name':'michaelma', 'age':30, 'gender':'male'}
# 输出所有的键
for each in my_dict.keys():
    print(each)

# 输出所有的键
for each in my_dict:
    print(each)

# 输出所有的键值
for (k, v) in my_dict.items():
    print(k, '-', v)