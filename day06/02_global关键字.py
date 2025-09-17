# global:
"""
作用：
    用来让函数的形参变量，变成全局变量
"""


a1 = 10
def f1():
    a1 = 20
f1()
print(f"a1 = {a1}")  # a1 = 10,说明a是形式参数
print('-' * 20)

a5 = 10
def f5():
    a5 = 20
f5()
print(f"a5 = {a5}")  # a1 = 10,说明a是实际参数
print('-' * 20)
"""
a2 = 10
def f2():
    a2 = 20     # global 语句必须放在函数内对变量的任何操作之前（包括赋值、读取等）。
    global a2   # 如果 global 声明之前有对变量的操作，Python 会认为它是一个局部变量，导致冲突。
f2()
print(f"a2 = {a2}")

"""

def f():
    global a3
    a3 = 10    # 只在函数中声明的全局变量，在函数外也可以使用
f()
print(a3)
print('-' * 20)




