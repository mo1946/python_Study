# 定义的三种形式:
    # 1. str1 = 'tom'
    # 2. str2 = "tom"
    # 3. str = """tom"""

name1 = 'tom1'
name2 = "tom2"
name3 = """tom3"""
print(f"name1 = {name1}\nname2 = {name2}\nname3 = {name3}")
print("-" * 20)

# 使用 """""" 可以保留换行细节
s = """
hi
hi
    """
print(s)
print("-" * 20)

# 想要输出 I'm is Tom.
    # 外双内单 如: "I'm is Tom"
    # 使用\'   \ 为转义符

str1 = "I'm is Tom"
str2 = 'I"m is Tom'  # 实际输出的是 I"m is Tom
str3 = 'I\'m is Tom'
print(f"str1 = {str1}\nstr2 = {str2}\nstr3 = {str3}")
print("-" * 20)

# 输出语句的结束标记
    # print("hi") == print("hi", end = '\n')  默认end为'\n'
print("hi")
print("hi", end = '\n')
print("hi", end = '')
print("hi", end = name1)
print()
print("-" * 20)

# 字符串切片
    # 模板 s[起始索引 : 结束索引 : 步长] 至少有一个分号不可以省，其余的可以按需求省略
str_1 = "abcdefgh"
# print
#
# 打印 bcde
print(str_1[1 : 5 : 1])
print(str_1[-7 : -3 : 1])
print("-" * 20)

# 打印 fedc
print(str_1[-3 : -7 : -1])
print(str_1[5 : 1 : -1])
print(str_1[5 : -7 : -1])
print(str_1[-3 : 1 : 1])
print("-" * 20)

# 如果 索引方向 和 步长方向相反，则无结果
print(str_1[-1 : 4 : 1])

# 字符串反转
print(str_1[::-1])
print(str_1[-1: -9 :-1])
print("-" * 20)

# 案例: 把字符串的前n个字符转移到字符串后面去 如 把abcdef的前三位转移到后面为 defabc
"""
while True:
    s = input("请输入不带空格的字符串: ")
    n = int(input("请输入要转移的个数: "))

    if n > len(s):
        print("没有这么多的数位,请重新输入：")
        continue
    else:
        s1 = s[:n:]
        s2 = s[n::]
        s3 = s2 + s1
        print(f"反转过后的字符串为: {s3}\n{s2}\n{s1}")
        break
print("-" * 20)

s = "sdfadfd"
print(s[:-1])
"""

s1 = 'abcdefgh'
# str里面一些常用的函数
    # s1.split()    将字符串按指定的分隔符分割成一个列表，可指定最大分割次数
    # s1.replace(原字符串， 替换单词， 替换个数)  将字符串中的指定子字符串替换为新的子字符串，返回替换后的新字符串，原字符串不变（因为字符串是不可变对象）。
    # '连接符'.join()     用指定的字符串将一个可迭代对象（如列表、元组）中的所有元素连接成一个新字符串。
    # '连接符'.join()     需要注意！非字符串元素会报错，需先转换
    # split() 默认按任意空白字符（包括空格、换行等）分割字符串
s = ''
l = ["Python", "is", "awesome"]
s = ' '.join(l)
print(s)

# 可以使用map(数据类型， 容器)，来转换成字符串类型的变量
l = [1, 2, 3, 4, 5]
s = ' '.join(map(str, l))
print(s)

s = 'I like apples'
s1 = 'apples'
s2 = 'bananas'
s3 = s.replace(s1, s2, 1)
print(s3)

s = "2023-10-25"
l = s.split('-')
print(l)
# 之后在使用.join()还原
s1 = '-'.join(l)
print(s1)
print('-' * 20)

# 案例
"""
给定字符串 "Hello, World! Python is fun!"，完成以下任务：
用 replace() 把 "Python" 替换成 "Java"。
用 split() 按空格分割成列表。
用 join() 把列表用 " | " 重新拼接。
示例输出:
    "Hello,|World!|Java|is|fun!"
"""

s = "Hello, World! Python is fun!"
s = s.replace("Python", "Java")
l = s.split()
s1 = '|'.join(l)
print(s1)
print("-" * 20)

# 案例
"""
文件路径处理
给定一个文件路径 "C:/Users/John/Documents/file.txt"
用 split() 和 join() 完成以下任务：
分割路径，提取文件名 "file.txt"。
把路径中的 / 替换成 \（Windows 风格）。
示例输出：
   
"""

s = "C:/Users/John/Documents/file.txt"
l = s.split('/')
fileName = l[4]
newPaths = '\\'.join(l)   # 因为\是转义字符要用\\来表示
print(f"文件名:{fileName}\n新路径:{newPaths}")









