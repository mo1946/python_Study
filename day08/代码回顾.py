

"""
本题为  Codeforces网站   H. 联觉信标

为什么用 python：
    这题是之前用c++做出来的，使用了打表法，
    但是，是自己一个一个复制粘贴打的表，很累
    因为学过 python 想用python实现自动打表
"""

data = """
* *
* **
* **
***
*
*
* *
***
* **
****
**
****
* *
* *
*
*****
**
***
* *
***
*** *
* ***
* **
* *
*
*****
* **
**
* *
**
*****
* *
***
** *
*****
*****
* *
***
**
*****
**
***
** **
**
*****
**
* *
**
* *
*****
* **
***
** *
* **
***
*****
**
**
* **
***
** *
** *
* *
* * *
***
* *
**
****
* **
*
*
***
* **
* **
* *
**
**
* *
* * *
***
**
* **
* *
* *
* **
*****
* **
* *
* * *
****
** *
** *
* *
****
* *
*****
* *
* *
* *
* *
*****
**
**
* * *
**
*****
*
**
* *
***
*****
**
***
* **
****
** *
****
** *
** **
** *
* *
* * *
* **
***
*
***
***
**
* *
*****
"""  # 替换为你的完整输入数据

s = [line for line in data.strip().split('\n')]
s1 = [s[i : i + 5] for i in range(0, len(s), 5)]
s2 = [''.join(liens) for liens in s1]
# print(s2)

# import string
# word = list(string.ascii_uppercase)   直接获取 A-Z 的列表
word = [chr(65 + i) for i in range(26)]
# print(word)

d = dict(zip(s2, word))
# print(d)

n = int(input())
s3 = ''
ans = ''
for i in range(n):
    ss = ''
    for j in range(5):
        s3 = input()
        ss += "".join(map(str,s3))
    ans += d.get(ss)
print(ans)

"""
* *
* **
* **
***
*
"""
import os

os.rename(r'B:\python\python_heiMa\day08\01.py', r'B:\python\python_heiMa\day08\代码回顾.py')



