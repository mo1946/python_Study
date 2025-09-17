
def calculator(my_func, a, b):
    """
    :param my_func: 要执行的运算
    :param a: 第一个参数
    :param b: 第二个参数
    :return: 返回的运算结果
    """
    return my_func(a, b)

print(calculator(lambda a, b : a + b, 10, 20))
print(calculator(lambda a, b : a - b, 10, 20))
print(calculator(lambda a, b : a / b, 10, 20))
print(calculator(lambda a, b : a * b, 10, 20))
print(calculator(lambda a, b : a ** b, 10, 20))
print(calculator(lambda a, b : a if a > b else b, 10, 20))
print(calculator(lambda a, b : min(a, b), 10, 20))

































