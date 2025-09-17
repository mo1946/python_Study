# 需求： 给 1.png 加密成 2.png 在解密成 3.png, 密码为20
# 核心： 原始字节 ^ 密码 ^ 密码 = 原始字节

src_f = open('date/1.png', 'rb')
dst_f = open('date/2.png', 'wb')

while True:
    date1 = src_f.read(1)
    if len(date1) == 0:
        break
    dst_f.write((date1[0] ^ 20).to_bytes())

src_f.close()
dst_f.close()
print("加密成功")
print('-' * 20)

password = int(input('请输出密码：'))
src_f = open('date/2.png', 'rb')
dst_f = open('date/3.png', 'wb')

while True:
    date1 = src_f.read(1)
    if len(date1) == 0:
        break
    dst_f.write((date1[0] ^ password).to_bytes())

src_f.close()
dst_f.close()
print("解密成功")




















