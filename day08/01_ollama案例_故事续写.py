"""
案例：故事续写

需求：通过 python 调用 API 实现 qwen 在 1.5b数据集下的文本续写

步骤：
    1. 导包
    2. 调用 ollama.chat()函数，并获得响应结果
    3. 从响应的结果中获得回复文本数据
    4. 打印到 "01_续写.txt" 文件中

注意：
    messages（输入）：复数，因为要传递多轮对话历史。
    message（输出）：单数，因为 API 每次只返回一条最新回复。
"""

import ollama
import os

response = ollama.chat(
    model = 'qwen2:1.5b',
    messages = [{'role' : 'user',
                 'content' : '我爱这一个人（续写这个故事，让这个故事有吸引力）'}]
)

# 注意 message 不要加s
# 1.
# out = response.message.content

# 2.
out = response['message']['content']

os.makedirs('./data', exist_ok=True)  # 确保文件夹的存在，如果没有就添加

with open('./data/01_续写.txt', 'w', encoding = 'utf-8') as f:
    f.write(out)
print('文件已保存至：data/01_续写.txt')


# 这里的知识都忘完了😣，学习学习，学习新知识，复习旧知识
























