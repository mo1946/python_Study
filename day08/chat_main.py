"""
用来充当 聊天机器人的前端模块，即：接受用户录入的信息，调用chat_utils模块的get_response()函数
并通过streamlit在前端界面调用即可
"""

import streamlit as st                                  # streamlit库：实现python代码的前端界面
from langchain.memory import ConversationBufferMemory   # langchain库：聊天机器人的核心， ConversationBufferMemory：聊天记录存储器
from chat_utils import get_response                     # 自定义模块：封装模型处理函数，获取模型的处理结果

st.title('(≧∀≦)ゞ')

if 'memory' not in st.session_state:
    st.session_state['memory'] = ConversationBufferMemory()
    st.session_state['messages'] = [{'role' : 'assistant', 'content' : '你好，我是智能聊天机器人，请问有什么可以帮助你的？'}]

for message in st.session_state['messages']:
    with st.chat_message(message['role']):
        st.markdown(message['content'])

prompt = st.chat_input('请输入你的问题')
if prompt:
    st.session_state['messages'].append({'role' : 'user', 'content' : prompt})
    st.chat_message('user').markdown(prompt)
    response = get_response(st.session_state['messages'])
    st.session_state['messages'].append({'role' : 'assistant', 'content' : response})
    st.chat_message('assistant').markdown(response)


