"""
捕获异常的语法格式：
    try:
        可能出现问题的代码

    except Exception as e:
            出现问题后的解决方案

    else:
        如果没有出问题，就执行里面的代码（即 没有执行 except ，就执行这里面）

    finally:
        无论是否有问题，都会执行里面的代码

"""

try:
    print(10 / 0)
except Exception as e:
    print(f'程序有问题: {e}')
else:
    print('程序没问题')
finally:
    print('这里时finally语句')



# 案例：优化猜数字游戏,让它可以处理有误的输入

import random

num = random.randint(1, 100)
while True:
    try:
        num1 = int(input('请输入一个1-100的整数: '))

        if num > num1:
            print('猜小了！')
        elif num < num1:
            print('猜大了！')
        else:
            print('猜对了，恭喜你！')
            break
    except:
        pass
























