l = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# while 遍历
i = 0
while i < len(l):
    print(l[i], end = ' ')
    i += 1
print()
print("-" * 20)

# for 遍历
for i in range(len(l)):
    print(l[i], end = ' ')
print()
print("-" * 20)

# 列表嵌套

ll = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# 输出 3
print(ll[0][2])
print(ll[-3][2])
print(ll[-3][-1])
print("-" * 20)

# 遍历
for i in range(len(ll)):
    for j in range(len(ll[i])):
        print(ll[i][j], end = ' ')
print()
print("-" * 20)

for i in ll:
    for j in i:
        print(j, end = ' ')
print()
print("-" * 20)

for i, sublist in enumerate(ll):
    for j, num in enumerate(sublist):
        print(f"ll[{i}][{j}] = {num}")


