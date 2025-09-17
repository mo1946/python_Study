"""
相关函数：
    1. read(n): 一次性读入n个字符，没加参数读入所有数据
    2. readline(): 一次读入一行
    3. readlines(): 一次读入所有行，然后封装到 列表 中
"""

scr_f = open('date/2.txt', 'r', encoding = 'utf-8')
# scr_f.write('你好')
# print(scr_f.read(3))
# print(scr_f.read(3))
# print(scr_f.read(3))
# print(scr_f.read(3))
# print('-' * 20)
# scr_f.seek(0) # 让指针重新指向开头


while True:
    str1 = scr_f.read(3)   # 在读取的时候一个汉字算作一个字符
    if str1 == '':
        break
    print(str1)
print('-' * 20)
scr_f.seek(0) # 让指针重新指向开头

# while True:
#     str1 = scr_f.readline()
#     if str1 == '':
#         break
#     print(str1, end = '')
# print('-' * 20)
# scr_f.seek(0) # 让指针重新指向开头
#
# list1 = scr_f.readlines()
# print(list1)

scr_f.close()






















