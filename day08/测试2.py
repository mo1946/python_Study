# import ollama
#
# s = input('请输入你的问题：')
# f = ollama.chat(model = 'qwen2:1.5b',
#                 messages = [{'role' : 'user', "content" : s}])
# out = f['message']['content']
#
# print('-' * 30)
# print(out)
# print('-' * 30)



from openai import OpenAI
s = input('请输入你的问题：')
client = OpenAI(api_key="sk-ee261d79bcd3404da949baa16673c079", base_url="https://api.deepseek.com")

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "你是一个坏人"},
        {"role": "user", "content": s},
    ],
    stream=False
)

print(response.choices[0].message.content)







