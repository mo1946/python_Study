name = "小妹"
age = 16
height = 1.58
flag = True

""" 
pycharm快捷键:
     格式化代码   ctrl + alt + L
     鼠标纵向选择 shift + alt + 鼠标选择
     代码上下移动 shift + alt + 方向键

代码格式
     print('她的名字叫' + name + '，今年' + str(age) + '，身高为' + str(height))
     print(f"她的名字叫{name}, 今年{age}, 身高为{height:05.3f}")
     print("她的名字叫{}, 今年{}, 身高为{}".format(name, age, height))
     print("她的名字叫%s, 今年%d, 身高为%.2f" % (name, age, height))
     print("状态: %s" % ("是" if flag else "否"))

代码解释与注意事项
     1.直接用print语句输出，但要注意用 + 连接 str 和 int 时要加 “,”不可以直接连接
     2.用f""来进行输出，{}里面装变量名
     3.用.format(变量名)格式进行输出，注意前面的是"."不是","
     4.用 % ()进行输出，和c语言差不多
     5.输出bool类型时 直接print(flag) 和 print("%s" % flag)都输出True，print(%d % flag)输出的是 1
     保留小数和填充固定长度和c语言差不多，保留小数会4舍5入
"""

