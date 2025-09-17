# 函数:
"""
    定义: 创建一个可重复使用的代码块的过程，通过给它命名、指定输入（参数）和功能（逻辑）
    语法:
        def 函数名 (形参1，形参2，....):   # 可选
            函数代码
            ...
            ...
            return 返回值   # 可选  无 return 时默认返回 None

    函数的主要优点：
        代码复用：避免重复编写相同代码
        模块化：将复杂问题分解为小任务
        易于维护：修改只需在一处进行

    注意点:
        函数只有在被调用的时候才会被执行
        函数内部定义的变量是局部变量，只在函数内部有效

    快捷键:
        ctrl + Q : 光标点到函数名时，可以参看函数的注释
"""

# 简单举例
def Greeting (name):
    """用来问候"""
    print(f"你好, {name}")

name = input("请输入姓名: ")
Greeting(name)
print('-' * 20)

# 打印5次 hello world
def hello_world():
    """
    :return: 返回5次hello_world
    """
    for i in range(5):
        print("hello world")
hello_world()
print('-' * 20)

def my_add_1(a):
    """
    :param a: 传入要要加 1 的数
    :return: 返回加 1 后的数
    """
    a += 1
    return a

a = 2
print(my_add_1(a))  # 3
print(a)            # 2
print('-' * 30)
# 这个案例说明传入的参数是形式参数，不会对函数外的参数有影响

# 案例 奇偶求和，给出一个数字的列表，分别求出奇数之和与偶数之和

def calculate_sum(list1):
    """
    :param list1: 待计算的数组
    :return: 返回奇数和偶数数组
    """
    sum1 = 0
    sum0 = 0
    for num in list1:
        if num % 2 == 1:
            sum1 += num
        else:
            sum0 += num
    list = [sum0, sum1]
    return list

numbers_list = [1,2,3,4,5,6,8,15,16,80,99]
list = calculate_sum(numbers_list)
print(f"奇数和为：{list[0]},偶数和为：{list[1]}")




















