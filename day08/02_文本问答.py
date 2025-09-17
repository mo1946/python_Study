import ollama

f = True
ss = 'qwen2:1.5b'

def ff():
    print("""
            ? : 参看指令
            handoff : 更换 ai 模型
            esc : 退出聊天
            """)

def hh():
    global ss
    print('-' * 50)
    print("""
                deepseek-r1:1.5b
                qwen2:1.5b
                qwen:0.5b
                    """)
    print('-' * 50)
    ss = input("请输入要更换的 ai 模型名称: ")

    print('更换成功!')

while True:
    if f == True:
        ff()
        f = False

    s = input('请输入你要询问的问题或指令：')
    if s.lower() == 'esc':
        break

    if s == 'handoff':
        hh()
        continue

    if s == '?':
        ff()
        continue

    response = ollama.chat(
        model = ss,
        messages = [{'role' : 'user',
                     'content' : s}]
    )
    out = response['message']['content']
    print('-' * 50)
    print(out)
    print('-' * 50)
    print()
print('欢迎下次使用！')










"""
说明:
    这是使用这个ai,它写的冒泡排序

def bubble_sort(arr):
    # 获取数组的长度
    n = len(arr)

    # 遍历所有的元素
    for i in range(n):
        # 从数组的第0个索引开始，进行一次比较
        for j in range(0, n - i - 1):

            # 如果当前元素大于下一个元素，则交换它们
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# 测试冒泡排序
arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print("排序后的数组是:")
for i in range(len(arr)):
    print("%d" % arr[i], end=" ")
"""


response = ollama.chat(model = 'deepseek-r1:1.5b',
                       messages = [{'role' : 'user', 'content' : '你是什么模型？'}]
                       )
out = response['message']['content']
print(out)































