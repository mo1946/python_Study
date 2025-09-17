import streamlit as st
from langchain.memory import ConversationBufferMemory
from hou import get_response
from datetime import datetime  # 新增时间模块

st.title('聊天机器人')

# 初始化会话状态
if 'memory' not in st.session_state:
    st.session_state['memory'] = ConversationBufferMemory()
    st.session_state['messages'] = [{
        'role': 'assistant',
        'content': '你好，有什么可以帮你的吗？',
        'time': datetime.now().strftime("%H:%M:%S")  # 记录初始消息时间
    }]

# 显示历史消息（带时间戳）
for message in st.session_state['messages']:
    with st.chat_message(message['role']):
        st.markdown(f"{message['content']}")
        st.caption(f"⏱️ {message['time']}")  # 在消息下方显示时间

# 用户输入处理
prompt = st.chat_input('输入')

if prompt:
    # 记录用户消息（含时间）
    user_message = {
        'role': 'user',
        'content': prompt,
        'time': datetime.now().strftime("%H:%M:%S")  # 记录用户发送时间
    }
    st.session_state['messages'].append(user_message)

    # 显示用户消息
    with st.chat_message('user'):
        st.markdown(prompt)
        st.caption(f"⏱️ {user_message['time']}")

    # 获取机器人响应
    with st.spinner('😴'):
        response = get_response(st.session_state['messages'])

    # 记录机器人响应（含时间）
    bot_message = {
        'role': 'assistant',
        'content': response,
        'time': datetime.now().strftime("%H:%M:%S")  # 记录机器人回复时间
    }
    st.session_state['messages'].append(bot_message)

    # 显示机器人响应
    with st.chat_message('assistant'):
        st.markdown(response)
        st.caption(f"⏱️ {bot_message['time']}")