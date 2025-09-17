from openai import OpenAI

def get(prompt):
    client = OpenAI(api_key="sk-13b5402d50794f99b3db499becce0820", base_url="https://api.deepseek.com")

    try:
        response = client.chat.completions.create(
            model='deepseek-chat',
            messages=prompt[-30:]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"出错啦: {str(e)}"
