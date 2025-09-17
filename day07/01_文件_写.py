"""
文件的操作:
    1. 打开文件:
            open('文件路径', '模式', '码表-可选')
            # 如果打开时没有此文件，Python会自动创建
    2. 写入数据：
            read()
            write()
    3. 关闭文件:
            close()

路径：
    1.绝对路径：以盘符开头的路径
    2.相对路径：在Python中，默认为相对于当前项目的路径来讲

"""

# 扩展：查看相对路径是以那个路径相对的
import os
print(os.getcwd())   # B:\python\python_heiMa\day_07


# 创建一个1.txt文件，往里面写入 "Hello Python"
"""
    'date\\1.txt', 'w'
    r'date\1.txt', 'w'  # r是用来忽视转义字符\的
    'date/1.txt', 'w' 
    这三种相对路径的写法都可以
"""
def_1 = open(r'B:\python\python_heiMa\day_07\date\1.txt', 'w')  # 返回值为一个文件的操作对象
n = def_1.write("Hello Python")      # 返回值为写入数据的字数（int）
print(type(n), n)
def_1.close()















































