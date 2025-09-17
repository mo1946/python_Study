# python中的列表list类似于c语言中的数组，但python中的列表元素可以是不同类型的元素

list1 = []
list2 = list()
list3 = [1, 2, 3, 4, 5]
list4 = [1, '2', 3.2, True]

print(f'list1 = {list1}')
print(f'list2 = {list2}')
print(f'list3 = {list3}')
print(f'list4 = {list4}')
print('-' * 20)

# 索引和c语言差不多，从0开始
print(list4[2])
print('-' * 20)

# 查                 ------------------------------------------------- * -------------------------------------------------
    # index(val, start, end) 用来返回在给定的范围里，第一次出现val的下标
    # count() 用来记录指定元素出现的次数
    # in() 用来判断该元素是否出现 输出bool值
    # not in() 和in()相反

list5 = [1, 2.3, '12', True, 1]
print(list5.index(1))
print(list5.count(1))    # 这里会输出3，因为True是int的子类值为1
print(2.3 in list5)
print(1 not in list5)
print('-' * 20)

# 增                 ------------------------------------------------- * -------------------------------------------------
    # .append()                用于在list末尾添加一个元素
    # .insert(下标位置， val)    用于在list指定位置添加一个元素
    # .extend()                将一个可迭代对象（如列表、元组、集合等）中的所有元素添加到列表末尾,单个元素要用[]括起来

l = [1, 2, 3, 4, 5]
l.append(6)
print(l)
l.insert(2, 10)
print(l)
l.extend(l)
print(l)
print('-' * 20)

# 改                 ------------------------------------------------- * -------------------------------------------------
    # .reverse()             用于反转列表
    # .sort(key, reverse)    用于对列表排序,里面元素要是同类型

l1 = [ 1, 2, 3, 10, 5, 6,]
l1.reverse()
print(l1)
l1.reverse()
l1.sort()
print(l1)
l1.sort(reverse = True)
print(l1)
print('-' * 20)

# 删                 ------------------------------------------------- * -------------------------------------------------
    # del  删除列表中的某个元素。
    # pop()  删除指定下标元素,默认最后一个,并返回干数据。
    # remove()  移除列表中某个数据的第一个匹配项。

ll = [ 1, 2, 3, 10, 5, 6,]
del ll[2]
print(ll)
num = ll.pop(2)
print(ll, num)
ll.remove(6)
print(ll)








