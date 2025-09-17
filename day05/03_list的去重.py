ll = [1, 1, 2, 2, 2, 3, 4, 5, 5, 6, 6, 8, 8]

# 案例 把ll数组进行去重，重复的元素只记录一次

l = list()
for i in ll:
    if i not in l:
        l.append(i)
print(l)
print("-" * 20)





