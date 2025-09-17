# 基础题:

# 1.已知列表 names_list =['乔峰"，'虚竹',"段誉"]，ages_list=[38，28，18]，
# 通过推导式，将其拼接成字典形式，并打印结果。


"""
zip() 是 Python 的一个内置函数，用于将多个可迭代对象（如列表、元组、字符串等）
按顺序配对，返回一个迭代器（zip 对象），
其中每个元素是一个元组，包含来自各个输入可迭代对象的对应位置的元素。

语法：
    zip(iterable1, iterable2, ...)
    1. 可以传入多个可迭代对象（如列表、元组、字符串等）。
    2. 返回一个 zip 对象（迭代器），可以用 list()、dict() 或 for 循环来遍历

"""
names_list =['乔峰', '虚竹', "段誉"]
ages_list=[38, 28, 18]
dc = dict(zip(names_list, ages_list))
print(dc)


# 2.自定义函数，接收整数，计算其平均值，调用该函数，并将结果打印到控制台上

def average(* args):
    """
    :param args: 传入的数据
    :return: 求平均值
    """
    sum1 = 0
    for num in args:
        sum1 += num
    return sum1 / len(args)

nums_list = [1, 2, 5, 6, 9, 15, 62]
print((average(* nums_list)))  # 直接传入容器，不要忘记用 * 解包


# 3.已知变量 a= 10，b=3，请写代码完成变量值交换，尽可能多的用不同的解决方案实现

a= 10
b=3
i = 0
print(f"第{i}次交换, a = {a}, b = {b}")
print('-' * 20)
i += 1

# 1. 拆包的方式
a, b = b, a
print(f"第{i}次交换, a = {a}, b = {b}")
print('-' * 20)
i += 1

# 2.用中间值来暂时保存
cmp = a
a = b
b = cmp
print(f"第{i}次交换, a = {a}, b = {b}")
print('-' * 20)
i += 1

# 用算数运算
a = a + b
b = a - b
a = a - b
print(f"第{i}次交换, a = {a}, b = {b}")
print('-' * 20)
i += 1

# 用位运算
a = a ^ b
b = a ^ b
a = a ^ b
print(f"第{i}次交换, a = {a}, b = {b}")
print('-' * 20)


# 进阶题:
# 2.最近回文数
# 需求:查找最近回文数,回文数是指从前往后读和从后往前读都是一样的数字，比如 121。
# 最近的回文数指的是离给定数字最近的回文数，比如给定数字 125，最近的回文数是121。
# 编写一个程序，查找离给定整数最近的回文数。



def Number_of_palindromes(s):
    """
    :param s: 传入的数字
    :return:  返回离给定整数最近的回文数
    """
    if len(s) & 1 == 1:
        return s[0 : len(s) // 2 + 1] + s[len(s) // 2 - 1 : : -1]
    else:
        return s[0: len(s) // 2] + s[len(s) // 2 - 1: : -1]

s = input('请输入一个数字: ')
print((Number_of_palindromes(s)))

# 其实上面的答案不完全对，比如输入129， 最近的应该是131， 而不是121


# 改正版：
def Number_of_palindromes1(s):
    """
    :param s: 传入的数字
    :return:  返回离给定整数最近的回文数
    """
    num_u = 0
    num_d = 0
    for num in range(int(s), 0):
        if(str(num) == str(num)[::-1]):
            num_d = num
            break
    for num in range(int(s), int(s) * 10):
        if(str(num) == str(num)[::-1]):
            num_u = num
            break
    print(num_u if num_u - num < num - num_d else (num_d if num_u - num > num - num_d else (num_d, num_u)))

s = input('请输入一个数字: ')
Number_of_palindromes1(s)



























