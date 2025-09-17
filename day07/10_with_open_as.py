"""
语法：
    with open('文件地址', '参数', encoding = '编码') as 变量名, open() as 变量名, .... :

用处：
    1. with语法执行完毕后会自动释放内存，无需手动释放
    2. 使代码更加简单

"""

"""
    src_f = open('date/1.txt', 'rb')
    dst_f = open('date/2.txt', 'wb')
    
    while True:
        date1 = src_f.read(1024)
        if len(date1) == 0:
            break
        dst_f.write(date1)
    
    src_f.close()
    dst_f.close()
"""

# 改写
with open('date/1.txt', 'rb') as src_f, open('date/2.txt', 'wb') as dst_f:
    while True:
        date1 = src_f.read(1024)
        if len(date1) == 0:
            break
        dst_f.write(date1)

    src_f.close()
    dst_f.close()















