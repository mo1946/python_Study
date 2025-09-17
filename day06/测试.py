# 计算水仙花
def f(num):
    num1 = num % 10
    num2 = num // 10 % 10
    num3 = num // 100
    return num == l[num1] + l[num2] + l[num3]

l = [i ** 3 for i in range(0, 10)]

for i in range(100, 1000):
    if f(i):
        print(i)
print('-' * 30)



# 假设账号为: itcast, 密码为: hmai。只给3次机会, 登陆失败要提示剩余次数。
account = "itcast"
password = "hmai"

f = 0
for i in range(0, 3):
    s = input("请输入账号：")
    ss = input("请输入密码：")
    if s == account and ss == password:
        print("正在登录...")
        f = 1
        break
    elif s == account and ss != password:
        print(f"密码错误，你还有{2 - i}次机会")
    elif s != account and ss != password:
        print(f"账号密码错误，你还有{2 - i}次机会")
    else:
        print(f"账号错误，你还有{2 - i}次机会")

if f == 0:
    print("请一天之后在尝试！")
else:
    print("登录成功！")


# 编写程序完成以下任务：
# 1. 让用户输入一个句子
# 2. 统计这个句子中有多少个单词
# 3. 找出最长的单词
# 4. 把句子中的所有单词首字母大写后打印出来

s = input("请你输入一个英文句子：")

# 统计单词数量
words = s.split()
cnt = len(words)

# 找出最长的单词
max_len = 0
longest_word = ""
for word in words:
    if len(word) > max_len:
        max_len = len(word)
        longest_word = word

# 所有单词首字母大写
da_xie = [word.capitalize() for word in words]
ss = ' '.join(da_xie)

# 输出结果
print("单词数量:", cnt)
print("最长的单词:", longest_word)
print("首字母大写后的句子:", ss)


a = 10
def my_a(a):
    a = 20
my_a(a)
print(a)





















