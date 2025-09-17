
# input()函数可以用来接受用户输入的信息
# 用法：变量名 = input("提示用户输入的信息")
# 细节input()函数返回的数据类型默认是str
# 可以用数据类型+(变量名)的方式，转换数据类型

age = input("Please output your age: ")
print(f"Your age is : {age}\nThe date type is : {type(age)}")
age = int(age)
print(f"Your age is : {age}\nThe date type is : {type(age)}")































































