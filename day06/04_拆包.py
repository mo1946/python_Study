"""
拆包的解释：
    快速的从容器中提取各个值的过程，称之为拆包
    把多个值放进容器中的过程称之为，组包

格式：
    my_list = [1, 2, 3, 4]    组包
    a, b, c, d = my_list      解包
"""

# 交换两个变量的值
s1 = 10
s2 = 5
print(s1, s2)
print('-' * 30)

# 思路1：临时变量
tmp = s1
s1 = s2
s2 = tmp
print(s1, s2)
print('-' * 30)

# 思路2：拆包
s1, s2 = s2, s1
print(s1, s2)
print('-' * 30)

# 思路3：算数运算
s1 = s1 + s2
s2 = s1 - s2
s1 = s1 - s2
print(s1, s2)
print('-' * 30)

# 思路4：位运算
s1 = s1 ^ s2
s2 = s1 ^ s2
s1 = s1 ^ s2
print(s1, s2)
print('-' * 30)
















































