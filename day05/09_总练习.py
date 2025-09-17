# 案例 随机分配办公室，8个老师随机分配到3个办公室
"""
    需求：
        定义列表，记录8个老师的信息，列如：names_list = ['A', 'B', 'C', ......]
        定义列表，记录办公室，例如：office_.1ist=[[],[],[]],每个元素都是该办公室的老师名。
        结果如下(随机分配的，不一定是这个，仅供参考)
        office_.1ist=[[老师1，老师3，老师5]，[老师2，老师4，老师6，老师7]，[老师8]]
"""
import random

names_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
office_list = [[], [], []]

for name in names_list:
    i = random.randint(0, 2)
    office_list[i].append(name)    # 有可能有办公室没有老师

print(office_list)
print('-' * 30)

# 改进: 确保每个办公室至少有一个老师

names_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
office_list = [[], [], []]

for i in range(len(office_list)):
    teacher = random.choice(names_list)
    office_list[i].append(teacher)
    names_list.remove(teacher)

for name in names_list:
    i = random.randint(0, 2)
    office_list[i].append(name)

print(office_list)
print('-' * 30)

# 约瑟夫环：
"""
    有 n 个人站成的环，编号 1 - n
    从 1 开始报数， 是 3 的倍数就出列，然后下一个人就从 1 开始，一直到只剩一个人
    输出最后一人的编号
"""

# 方法一：模拟
n = int(input("请输入人数n: "))
person_list = []

for i in range(1, n + 1):
    person_list.append(i)

cnt = 0
index = 0
while len(person_list) > 1:
    cnt += 1
    if cnt == 3:
        cnt = 0
        person_list.pop(index)
    else:
        index += 1
    if index >= len(person_list):
        index = 0
print(person_list[0])
print('-' * 30)

# 方法二：双端队列

from collections import deque

n = int(input("请输入人数n: "))
q = deque(range(1, n + 1))

while len(q) > 1:
    q.rotate(-2)  # 前 2 人移到末尾，第 3 人变队首
    q.popleft()   # 删除第 3 人
print(q[0])









