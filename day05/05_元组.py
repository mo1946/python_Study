# 元组(tuple):
"""
与列表的不同点：
    1.元组与列表相比，元组的值不可以改变，所以没有增删改的操作，只有查
    2.与列表相比，它的性能上更优，所以在存储常数数据时用元组较好
    3.格式：列表是[], 元组是()

与列表相同点：
    1.均保持元素的插入顺序。
    2.可以存储不同类型的元素（如 [1, "a", True]）
    3.均支持索引、切片、迭代、len()、in 等操作

相互转换：
    1.通过 list() 和 tuple() 函数可以互相转换

涉及到的函数：
    1.index()
    2.len()
    3.count()
"""

tuple1 = (1, 2, 3)
tuple2 = tuple()
tuple3 = (1,)  # 当元组只有一个元素时，末尾要加逗号
tuple4 = ()
tuple5 = (1)   # 否则为int类型
print(f"tuple1 = {tuple1}")
print(f"tuple2 = {tuple2}")
print(f"tuple3 = {tuple3}")
print(f"tuple4 = {tuple4}")
print(f"tuple5 = {tuple5}")

print(f"tuple1 = {type(tuple1)}")
print(f"tuple2 = {type(tuple2)}")
print(f"tuple3 = {type(tuple3)}")
print(f"tuple4 = {type(tuple4)}")
print(f"tuple5 = {type(tuple5)}")
print('-' * 30)

# 演示函数
tup = (1,2,3,4,5,6,7,8,9,1)
print(tup[2])
print(len(tup))
print(tup.count(1))
print(tup.index(1))
print('-' * 30)

# 元组的嵌套
tupl = (1, 2, 3, [1, 2, 3])
tupl[3][1] = 11
print(tupl)
l = tupl[1:3] + tuple(tupl[3])
print(l)