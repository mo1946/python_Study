# 字典(dict)：
"""
定义：
    字典用花括号 {} 定义，键和值之间用冒号 : 分隔，键值对之间用逗号 , 分隔。
核心用途：
    1.快速查找数据：通过键（key）直接访问对应的值（value），时间复杂度为 O(1)，效率极高。
    2.存储关联数据：适合表示现实中的映射关系（如用户信息、配置项等）
    3.动态增删改数据：字典是可变的，可以随时添加、修改或删除键值对
    4.灵活的数据结构：键可以是不可变类型（如字符串、数字、元组），值可以是任意类型（甚至嵌套字典）

常用操作：
    1.获取所有键或值：keys(), values()
    2.遍历字典：for key, value in my_dict.items()
    3.检查键是否存在：if "name" in my_dict

"""

dict1 = {"name" : "小妹", "age" : 18}
dict2 = {}
dict3 = dict()
print(dict1)
print(dict2)
print(dict3)
print(f"dict3{type(dict1)}")
print(f"dict3{type(dict2)}")
print(f"dict3{type(dict3)}")
print(dict1["name"])


# 字典的增删改查
dict1 = {1 : "A", 2 : "B", 3 : "C"}

# 增
dict1[4] = 'D'
print(dict1)
print('-' * 30)

# 删
del dict1[1]
print(dict1)
print('-' * 30)
    # pop()：删除指定键并返回对应的值（避免KeyError异常时可设置默认值）
    #value = dict1.pop(2)           删除键2，返回'B'
    # value = dict1.pop(99, None)   键不存在时返回None（避免报错）

# 改
dict1[2] = 'R'
print(dict1)
print('-' * 30)

# 查
print(dict1.keys())
print(dict1.values())
print(dict1.items())
print('-' * 30)
    # 避免KeyError：用get()替代直接访问
"""
    print(dict1.get(1))     # 返回'A'（键存在）
    print(dict1.get(99))    # 返回None（键不存在）
    print(dict1.get(99, "默认值"))  # 返回"默认值"
"""


# 案例 记录字符出现的次数
s = input("请输入一个没用空格的字符串: ")
dict1 = dict()
for c in s:
    if c not in dict1.keys():
        dict1[c] = 1
    else:
        dict1[c] += 1

for key in dict1.keys():
    print(f"{key} : {dict1[key]}")
print('-' * 30)

# 推导式求字典

l = ['a', 'b', 'c', 'd']
ll = ['A', 'B', 'C', 'D']

dict1 = {ll[i] : l[i] for i in range(0, 4)}
print(dict1)
print('-' * 30)

# 没有元组推导式，只有生成器
numbers = (x for x in range(5))  # 返回生成器对象，不是元组！
print(type(numbers))  # <class 'generator'>

gen = (x ** 2 for x in range(5))
print(next(gen))  # 0（第一次迭代时计算）
print(next(gen))  # 1（第二次迭代时计算）


