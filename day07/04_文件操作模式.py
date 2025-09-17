"""
模式：
    1. w: 只写，字符模式
    2. r: 只读，字符模式
    3. a: 追加，字符模式

    1. wb: 只写，字节模式
    2. rb: 只读，字节模式
    3. ab: 追加，字节模式

    世界      2个字符，utf-8：6个字符，gdk：4个字节
    sj       2个字符，utf-8：2个字符，gdk：2个字节

使用：
    1. 以后拷贝文本文件，既可以用 r,w,a 也可以用 r+，w+，a+
    2. 图片的话一般用 r+，w+，a+

常见的文件分类
    文本文件：.txt, .csv, .json 等，可直接用文本模式打开。
    二进制文件：.jpg, .png, .exe, .pdf 等，必须用 'rb' 或 'wb'。
"""

# 按字符读取
f = open('date/2.txt','r',encoding = 'utf-8')
print(f.read(3))
f.close()
print('-' * 20)

# 按字节读取
# f = open('date/2.txt','rb',encoding = 'utf-8')  用字节查看时不可以加encoding参数
f = open('date/2.txt','rb')
str1 = f.read(3) # 在utf-8中一个汉字代表3个字节,所以读取3个
print(str1)
f.close()
print('-' * 20)

# 解码，即：字节 -> 字符
str2 = str1.decode('utf-8')
print(str2)
print('-' * 20)

# 读取图片
# f = open('date/1.png','r',encoding = 'utf-8') # 读取图片不可以用encoding参数
f = open('date/1.png','rb')
str3 = f.read()
print(str3)
f.close()
print('-' * 20)












































