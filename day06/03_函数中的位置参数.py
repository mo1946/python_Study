
def f(name, age, gender):
    print(f"name = {name}, age = {age}, gender = {gender}")

# 位置传参
# 按照参数在函数定义中的顺序依次传递值，位置必须严格对应
f('小明', 18 , '男')
print('-' * 30)

# 关键字传参
# 通过参数名直接指定值，无视参数顺序，精准传递
f(name = '小明', age = 18 , gender = '男')
print('-' * 30)

# f(name = '小明', 8 , gender = '男')  # 想混用位置参数和关键字传参，必须前面使用位置传参，即使位置相同也不行。
# print('-' * 30)

# 比如:
f('小明', age = 18 , gender = '男')
print('-' * 30)

f('小明', gender = '男', age = 18 )
print('-' * 30)

# 默认参数
def greet(name, age=30):  # age 有默认值
    print(f"Hello {name}, you are {age} years old.")

greet("Bob")          # 输出: Hello Bob, you are 30 years old.
greet("Bob", 40)      # 覆盖默认值，输出: Hello Bob, you are 40 years old.
greet(age=30, name = "Bob")      # 可以用关键字传参交换位置
print('-' * 20)
# 注意
    # 默认参数必须定义在非默认参数之后

# 不定长参数：
"""
    # *args：接收不定数量的位置参数
    
    def sum_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

print(sum_numbers(1, 2, 3))        # 输出: 6
print(sum_numbers(10, 20, 30, 40)) # 输出: 100

    # 注意：
        *args 将所有传入的位置参数打包成一个 元组（tuple）
        参数名 args 是约定俗成的，但可以替换为其他名称（如 *numbers）
"""

"""
    # **kwargs：接收不定数量的关键字参数
    
    def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25, city="New York")
    
# 注意：    
    **kwargs 将所有关键字参数打包成一个 字典（dict）
    参数名 kwargs 是约定俗成的，可替换为其他名称（如 **details）
    **kwargs 必须放在所有参数（包括 *args）之后
        如果反过来（**k 在前），解释器无法确定位置参数应该从哪里开始，因此语法直接禁止
    注意: 
        默认参数必须在*args之前：确保位置参数能明确分配。(在python 3+ 中可以)
        *args之后可以有关键字参数（Python 3+），但必须通过关键字传递。
        
"""

def my_print(name, age, * hobby, ** close_relatives):
    print(f"我的名字是：{name}"'\n'f"我的年龄是：{age}")
    print(f"我的爱好有：", end = '')
    for h in hobby:
        print(h, end=' ')
    print()
    print(f"我的亲人有：", end='')
    for key, value in close_relatives.items():
        print(f'{key}是我的{value}', end = ' ')

name = "小明"
age = 18
hobby_list = ['跑步', '游泳']
close_relatives_dict = {"小月" : "妹妹", "小华" : "哥哥"}
my_print(name, age, *hobby_list, **close_relatives_dict)
print()
print('-' * 20)
    # args 用于接收可变数量的位置参数，调用时可以直接传多个参数，或者用 *list 解包列表。
    # **kwargs 用于接收可变数量的关键字参数，调用时可以直接传 key=value，或者用 **dict 解包字典。


# def f(name, age = 18, *list, **dict)   可以
# def f(age = 18, name, *list, **dict)   不可以，直接报错，因为位置参数 name 不能出现在关键字参数 age=18 之后
# def f(name, *list, age = 18, **dict)   可以，但必须用关键字传参的方式,所以用默认参数没什么意义
# def f(name, *list, **dict, age = 18)   不可以,**dict 必须在最后

# 结论：在Python 3+ 版本中，只有**dict有强制性的位置要求，其他的位置参数，默认参数，不定长参数没有强制性要求

# def f(name, *list, age = 18, **dict)   可以，但必须用关键字传参的方式
    # 举例：
def f(name, *list, age=18, **dict):
    print(name, list, age, dict)
f(1, 1, 2, 3, 4, age = 18,a = 1,b = 2)
print('-' * 20)


# 关键结论
"""
    **kwargs 必须放在最后，默认参数不可以写在位置参数前，这是唯二强制性的顺序。
    其他参数（位置、默认、*args）的顺序需遵循：
    默认参数不能在 *args 之后（除非作为仅关键字参数）。
    位置参数不能在关键字参数后。
    Python 3 的仅关键字参数（通过 *, 或 *args 后的默认参数）提供了更灵活的设计方式。
"""






