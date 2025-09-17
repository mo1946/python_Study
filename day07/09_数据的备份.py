# 要求把 1.txt 备份一份 1[备份].txt

src_name = './date/1.txt'

idx = src_name.rfind('.')
new_src_name = src_name[:idx] + '[备份]' + src_name[idx:]

src_f = open(src_name, 'rb')
dst_f = open(new_src_name, 'wb')

while True:
    date = src_f.read(1024)
    if not date:
        break
    dst_f.write(date)

src_f.close()
dst_f.close()












