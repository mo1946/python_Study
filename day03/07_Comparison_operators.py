"""
比较运算符

    ==          等于（两个等于）
    !=          不等于
    >           大于
    >=          大于等于
    <           小于
    <=          小于等于

细节：
    1. 运算结果为 bool值
    2. 不要把 == 写成 = 否则得到的结果可能不是你想要的
"""
a, b = 10, 5

print(a == b)       # -> False
print(a != b)       # -> True
print(a > b)        # -> True
print(a >= b)       # -> True
print(a < b)        # -> False
print(a <= b)       # -> False