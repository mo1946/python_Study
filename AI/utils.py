import ollama

def get_response(prompt):
    response = ollama.chat(model = 'qwen2:1.5b',
                           messages = prompt[-30:])
    return response['message']['content']


if __name__ == '__main__':
    prompt = '请你写一首诗歌'
    print(get_response(prompt))



