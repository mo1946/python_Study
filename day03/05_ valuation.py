"""
赋值运算符：
    =        赋值运算符      # 把右边的赋值给左边

复合赋值运算符
# 就相当把计算的结果再赋值给左边的变量

    +=          加         # a += b -> a = a + b
    -=          减         # a -= b -> a = a - b
    *=          乘         # a *= b -> a = a * b
    /=          除         # a /= b -> a = a / b
    //=        整除        # a //= b -> a = a // b
    %=         求余        # a %= b -> a = a % b
    **=       幂指数       # a **= b -> a = a ** b

"""

# 例题，输入总账单，在其中加收20%的服务税，在均摊给每位顾客，保留1位小数

n = int(input("请你输入人数："))
total_bill = float(input("请你输入账单总款："))
total_bill *= 1.2
money = total_bill / n
print(f"每人要支付{money:.1f}元")