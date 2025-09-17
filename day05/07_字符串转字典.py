# A=a,B=b,C=c,D=d

s = input("请输入一个字符串(形式如: 'A=a,B=b'): ")
my_dict = {}
for str1 in s.split(','):
    list1 = str1.split('=')
    k, v = list1[0],list1[1]
    my_dict[k] = v
print(my_dict)

# print(my_list)


















