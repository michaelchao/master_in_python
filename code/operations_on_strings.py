#! -*- utf-8 -*-

# sample是个生成器
def sample():
    yield "Is"
    yield "Chicago"
    yield "Not"
    yield "Chicago?"

# 看起来join函数可以接收生成器
text = ''.join(sample())
print(text)
# IsChicagoNotChicago?

import sys
for part in sample():
    sys.stdout.write(part)
sys.stdout.write('\n')
# IsChicagoNotChicago?

# 通过这个例子可以学习生成器如何调用生成器
def combine(source, maxsize):
    parts = []
    size = 0
    for part in source:
        parts.append(part)
        size += len(part)
        # 当size大于阈值的时候，理解返回当前值
        if size > maxsize:
            yield ','.join(parts)
            parts = []
            size = 0
    yield ''.join(parts)

for part in combine(sample(), 6):
    sys.stdout.write(part)
sys.stdout.write('\n')