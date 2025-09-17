"""
模块解释：
    概述：
        在python中，把 .py 文件称之为 -> 模块
    分类：
        python内置模块:
            random, os, shutil, math, time
        自定义模块:
            创建的.py文件就是一个模块

    导入模块的方式:
        1. import 模块名
        2. import 模块名 as 别名

        3. from 模块名 import 功能名
        4. from 模块名 import 功能名 as 别名
        5. from 模块名 import *

    区别：
        1. import 模块名 方式
            A. 可以调用改模块下的所有功能
            B. 必须通过 模块名.功能名() 的方式调用

        2. from 模块名 import 功能名 方式
            A. 只能使用 导入的 功能名
            B. 可以通过 功能名() 直接调用
"""


# import time
# time.sleep(3)
# print('睡醒了')

# import time as t
# t.sleep(2)
# print('睡醒了')

# from time import sleep
# sleep(2)
# print('睡醒了')

# from time import sleep as s, time as t
# s(3)
# print(t())

# from time import *
# sleep(2)
# print(time())


"""
__name__ == '__main__':
    简介：
        它是python模块的内置变量，只要是.py文件都有这个变量
        直接运行时：__name__ 会被赋值为 '__main__'
        被导入时：__name__ 会被赋值为模块的文件名（不含 .py 后缀）
        
    作用：
        区分模块是被导入还是直接运行：
            通过判断 __name__ 的值，可以让同一份代码在被导入时执行某些逻辑，而直接运行时执行其他逻辑。
        避免导入时执行测试代码：
            如果模块中有测试代码或示例代码，放在 if __name__ == '__main__': 块中可以确保这些代码仅在直接运行时执行，而被导入时不执行。
        提供模块的入口点：
            类似于其他语言的 main() 函数，用于定义模块的“主程序”逻辑。

"""























