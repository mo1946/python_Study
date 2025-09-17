"""
lambda表达式：又称之为匿名函数，是 Python 中一种简洁的定义单行函数的方式

格式：
    lambda 参数1, 参数2, ... : 表达式
参数：
    可以接受多个参数，用逗号分隔（类似普通函数的参数）
表达式：
    只能有一个表达式，其计算结果就是返回值（不能写 return）


lambda 和 def函数的区别：
    1. lambda函数没有函数名
    2. Lambda 只能包含一个表达式，不能包含复杂的逻辑（如循环、多行代码）

使用场景：
    1. 如果函数逻辑非常简单，且只在一处使用，用 Lambda 更简洁
    2. Lambda 常用于 map()、filter()、sorted() 等需要函数作为参数的场景

"""

# 如：
add  = lambda a, b : a + b
print(add(10, 20))
print("-" * 20)

# 比较两个数之间的最大值
my_max = lambda a, b : a if a > b else b
print(my_max(12, 15))

# 利用sort函数进行自定义排序
d = [
    {'name' : "张三", 'age' : 15},
    {'name' : "李四", 'age' : 22},
    {'name' : "王五", 'age' : 20}
]

# d.sort()
# print(d) # 直接比较会报错，因为d列表中的元素是字典，而字典是不可以排序的

# 按照name排序，默认顺序是a，b，c...
d.sort(key = lambda d : d['name'])  # Python 默认按汉字的 Unicode 编码排序（拼音顺序可能不符合预期）
print(d)
print('-' * 100)

# 按照age排序
d.sort(key = lambda x : x['age'])
print(d)
d.sort(key = lambda x : x['age'],reverse = True)
print(d)









