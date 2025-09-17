"""
该模块从当 聊天机器人的后端 即：接受前端（streamlit）传来的请求，
在这里通过大语言模型的处理，在返回前端
"""
import ollama

def get_response(prompt):
    """
    :param prompt: 代表用户问答的最近20条历史记录
    :return: 返回处理语句
    """
    response = ollama.chat(model = 'qwen2:1.5b',
                           messages = prompt[-20:])
    return response['message']['content']

if __name__ == '__main__':
    prompt = '给我写一首诗句，关于人生的(长一点)：'
    response = get_response(prompt)
    print(response)



















