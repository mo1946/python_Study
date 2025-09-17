# 案例 编写一个代码让玩家在1 - 100里面猜一个随机数字


import random

idea = '?'
while idea == '?' or idea == 'Y':
    ai = random.randint(1, 100)
    gamer = int(input("请输入一个1 - 100里面的数字: "))
    while ai != gamer:
        if ai > gamer:
            print("小了")
            gamer = int(input("请输入一个1 - 100里面的数字: "))
        elif ai < gamer:
            print("大了")
            gamer = int(input("请输入一个1 - 100里面的数字: "))

    print("猜对了")
    idea = input("还想再玩吗(Y or N): ").strip().upper()

print("再见")