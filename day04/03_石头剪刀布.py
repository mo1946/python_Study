# 玩家 和 电脑 (随机出)
# 1为石头， 2为剪刀， 3为布

import random

def rock_paper_scissors():
    print("石头剪刀布游戏")
    print("1: 石头")
    print("2: 剪刀")
    print("3: 布")
    print("输入q退出游戏")

    while True:
        # 玩家输入
        player_choice = input("请出拳(1/2/3): ").strip().lower()

        # 退出条件
        if player_choice == 'q':
            print("游戏结束")
            break

        # 验证输入
        if player_choice not in ['1', '2', '3']:
            print("无效输入，请重新输入1、2或3")
            continue

        player = int(player_choice)
        computer = random.randint(1, 3)

        # 显示双方选择
        choices = {1: "石头", 2: "剪刀", 3: "布"}
        print(f"你出: {choices[player]}，电脑出: {choices[computer]}")

        # 判断胜负
        if player == computer:
            print("平局！再来一次")
            continue

        # 胜负规则
        if (player == 1 and computer == 2) or \
                (player == 2 and computer == 3) or \
                (player == 3 and computer == 1):
            print("你赢了！")
        else:
            print("你输了！")

        # 询问是否继续
        play_again = input("再玩一次？(y/n): ").strip().lower()
        if play_again != 'y':
            print("游戏结束")
            break


# 启动游戏
rock_paper_scissors()
        