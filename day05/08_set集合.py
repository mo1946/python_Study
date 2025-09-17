# set 是 Python 中的一种无序、可变、不重复元素的集合数据类型。它类似于数学中的集合概念，支持交集、并集、差集等操作。

"""
集合的特性:
    1.无序：集合的元素没有固定顺序，每次打印可能顺序不同
    2.元素唯一（自动去重）：
    3.只能存储不可变类型（可哈希对象）
        可以存储：int, float, str, tuple（不可变类型）
        不能存储：list, dict, set（可变类型）

集合的常用操作：
    1.添加元素
        add()：添加单个元素
        update()：添加多个元素（可传入列表、元组、集合等）

    2.删除元素
        remove()：删除指定元素（元素不存在则报错）
        discard()：删除指定元素（元素不存在也不报错）
        pop()：随机删除并返回一个元素（集合无序）
        clear()：清空集合

    3.查找元素
        in: 在就返回 True，否则 False
        not in: 和 in 相反

集合运算（数学集合操作）：
    1.并集（Union）
       A = {1, 2, 3}
       B = {3, 4, 5}
       print(A | B)          # 输出：{1, 2, 3, 4, 5}
       print(A.union(B))     # 同上

    2.交集（Intersection）
        print(A & B)          # 输出：{3}
        print(A.intersection(B))  # 同上

    3.差集（Difference）
        print(A - B)          # 输出：{1, 2}（A 有但 B 没有的）
        print(A.difference(B))  # 同上

    4.对称差集（Symmetric Difference）
        print(A ^ B)          # 输出：{1, 2, 4, 5}（A 和 B 独有的元素）
        print(A.symmetric_difference(B))  # 同上

"""

set1 = {1,2,3,4,5,5}
set2 = set()
set3 = {}
print(set1)
print(set2)
print(set3)
print(f"set1 = {type(set1)}")
print(f"set2 = {type(set2)}")
print(f"set3 = {type(set3)}")   # set3 = {} 是字符串
print('-' * 30)

# 案例 给list1 = [1,2,3,4,5,6,5,4,2]去重
list1 = [1,2,3,4,5,6,5,4,2]
set1 = set(list1)
list2 = list(set1)
print(list2)

# 案例 计算缺失的值
list1 = [1,1,2,3,5,2,4,5,6,7,4, 9, 15]
set1 = set(list1)
list2 = list(set1)
sum = 0
ans = []
for num in range(min(list2), max(list2) + 1):
    if num not in list2:
        ans.append(num)
        sum += num
print(ans,sum)
print('-' * 30)










