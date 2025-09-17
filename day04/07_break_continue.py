# break 用来跳出一层循环
# 结束本次的循环，执行下一次

# 案例 补充完整，使得实现指定的功能

"""
i = 0
while i <= 10:
    i += 1
    if i % 3 == 0:
        #请在次填入一行代码
    print("hi")
"""


# 输出两次hi
i = 0
while i <= 10:
    i += 1
    if i % 3 == 0:
        break
    print("hi")
print("-" * 20)



# 输出7次hi
i = 0
while i <= 10:
    i += 1
    if i % 3 == 0:
        continue
    print("hi")
print("-" * 20)



# 输出13次hi
i = 0
while i <= 10:
    i += 1
    if i % 3 == 0:
        print("hi")
    print("hi")
print("-" * 20)
