# 把 1.txt 的内容反转存入 2.txt

src_f = open('date/1.txt', 'r', encoding = 'utf-8')
dst_f = open('date/2.txt', 'w', encoding = 'utf-8')

while True:
    date1 = src_f.readline()
    if len(date1) == 0:
        break
    date1 = date1[::-1]
    dst_f.write(date1)

src_f.close()
dst_f.close()




























