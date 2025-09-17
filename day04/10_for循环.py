# 格式: for i in 容器类型:
for i in "python":
    print(i, end = '')
print()
print('-' * 20)

# range(起点 , 终点 , 步长)
# 在Python中，range() 是一个内置函数，用于生成一个不可变的整数序列（通常用于循环）
# range(stop)                # 生成 0 到 stop-1 的整数序列
# range(start, stop)         # 生成 start 到 stop-1 的整数序列
# range(start, stop, step)   # 生成 start 到 stop-1，步长为 step 的序列

print(range(10))
for i in range(0, 10, 1):
    print(i, end = ' ')
print()
print('-' * 20)

# 案例1 计算1-100之间的偶数和
sum = 0
for i in range(0, 101, 2):
    sum += i
    # print(i)
print(sum)
print('-' * 20)

# 循环加else语法:
"""
for ...
    ...
    ...
else:


while ...
    ...
    ...
else:

"""

"""
在Python中，for-else 和 while-else 是两种特殊的循环结构，
它们的 else 块会在循环正常结束（即未被 break 中断）时执行。
如果循环被 break 终止，else 块不会执行。
"""
for i in range(11):
    print(i)
    if(i == 10):
        break
else:
    print("^-^")
print('-' * 20)

for i in range(11):
    print(i)
else:
    print("^-^")
print('-' * 20)

# 案例：输出1-100中的质数，并且3个为一行
# 1.
f = 0
cnt = 0
for i in range(2 , 101):
    for j in range(2 , i):
        if i % j == 0:
            f = 1
            break
    if f == 0:
        cnt += 1
        print(i, end = ('\n' if cnt == 3 else ' '))
    if cnt == 3:
        cnt = 0
    f = 0
print()
print("-" * 20)

# 2.
count = 0  # 用于控制每行输出的质数个数
for num in range(2, 101):
    # 检查 num 是否为质数
    for i in range(2, int(num ** 0.5) + 1):  # 优化：只需检查到平方根
        if num % i == 0:
            break  # 如果能整除，说明不是质数，跳出循环
    else:
        # 如果 for 循环正常结束（没有 break），说明 num 是质数
        print(num, end=' ')  # 不换行，用空格分隔
        count += 1

        # 每输出 3 个质数换行
        if count % 3 == 0:
            print()  # 换行

