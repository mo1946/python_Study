# 案例一：拷贝 1.txt -> 复制到 2.txt
# 1. 用字符模式
# src_f = open('date/1.txt', 'r', encoding = 'utf-8')
# dst_f = open('date/2.txt', 'w', encoding = 'utf-8')
#
# while True:
#     date1 = src_f.read(1024)
#     if len(date1) == 0:
#         break
#     dst_f.write(date1)
#
# src_f.close()
# dst_f.close()

# 2. 用字节模式
src_f = open('date/1.txt', 'rb')
dst_f = open('date/2.txt', 'wb')

while True:
    date1 = src_f.read(1024)
    if len(date1) == 0:
        break
    dst_f.write(date1)

src_f.close()
dst_f.close()


# 案例二: 拷贝 1.png -> 复制到 2.png

src_f = open('date/1.png', 'rb')
dst_f = open('date/2.png', 'wb')

while True:
    date1 = src_f.read(1024)
    if len(date1) == 0:
        break
    dst_f.write(date1)

src_f.close()
dst_f.close()


























