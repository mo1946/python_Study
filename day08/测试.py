import os
import time
import ollama

response = ollama.chat(
    model = 'qwen2:1.5b',
    messages = [{'role' : 'user',
    'content' : '现在让你扮演一个哲学家，请问人生应当如何度过：'}]
)

out = response['message']['content']

with open('data/2.txt','wb') as f:
    f.write(out.encode('utf-8'))

print('进行打印中...')

for i in range(1, 4):
    time.sleep(1)
    print(i)
print("打印成功")































