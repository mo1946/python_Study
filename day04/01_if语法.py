"""
核心：
    1.顺序执行
    2.判断条件
"""

# 案例一（单分支）
# 判断用户是否可以上网
print("如果什么多都没讲，默认不可以上网")
age = int(input("请输入你的年龄："))
if age >= 18:
    print("可以上网")

# 案例二（双分支）
# 判断用户是否可以上网
age = int(input("请输入你的年龄："))
if age >= 18:
    print("可以上网")
else:
    print("你还没成年，不可以上网")

# 案例三（多分支）
# 判断一年四季
month = int(input("请输入月份："))
if month == 12 or month == 1 or month == 2:
    print("冬天，请保暖")
elif month >= 3 and month <= 5:
    print("春天，多走走")
elif 6 <= month <= 8:
    print("夏天，多走走")
elif month in [9, 10, 11]:
    print("秋天，很凉快")
else:
    print("没有这样的月份，懂？")