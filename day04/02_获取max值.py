# 判断两个数中的最大值

# 1.if条件判断
a = 50
b = 200
max_int = -1
if a >= b:
    max_int = a
else:
    max_int = b
print(max_int)
print("-" * 20)

# 2.三元表达式
# 格式：值一 if 判断条件 else 值二
a1 = 20
b1 = 30
# print(f"{a1 if a1 >= b1 else b1}")
max_int1 = a1 if a1 >= b1 else b1
print(max_int1)
print("-" * 20)


# 判断三个数中的max值

# 1.if条件判断
a, b, c = 10000, 2000, 30
max_int2 = 0
if a >= b and a >= c:
    max_int2 = a
elif b >= a and b >= c:
    max_int2 = b
else:
    max_int2 = c
print(max_int2)
print("-" * 20)

# 2.三元表达式
a = 10
b = 20
c = 30
max_int3 = (a if a >= c else c) if a >= b else (b if b >= c else c)
print(max_int3)
print("-" * 20)


# 案例：判断是否是酒驾
# 酒精含量 >= 20mg/100ml 为酒驾
# 酒精含量 >= 80mg/100ml 为醉驾
con = int(input("请输入酒精含量:"))
if con >= 80:
    print("醉驾")
elif con >= 20:
    print("酒驾")
else:
    print("安全")
print("-" * 20)