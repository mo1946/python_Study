# 1.输入一个字符串，计算其中字符出现的次数

s = input("请输入字符串: ")
ss = ''
for c in s:
    if c not in ss:
        ss += c   # 去重
for i in ss:
    cnt = 0
    for j in s:
        if i == j:
            cnt += 1
    print(f"{i}出现的次数：{cnt}")
print("-" * 20)


# 2. 统计没有出现的数字，并返回他们的总和(没出现的数字是指最大值和最小值之间的没出现的数字)

l = [1, 2, 5, 9, 6, 10, 10, 5, 5]  # 没出现的数字是3 4 6 7 8
full_set = set(range(min(l), max(l)))
ll = sorted(full_set - set(l))
print(f"没出现的数字有{ll}")

