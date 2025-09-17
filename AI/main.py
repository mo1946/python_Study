
import streamlit as st
from langchain.memory import ConversationBufferMemory
from utils import get_response

st.title('<(￣︶￣)↗[AI!]')

if 'memory' not in st.session_state:
    st.session_state['memory'] = ConversationBufferMemory()
    st.session_state['messages'] = [{'role': 'assistant', 'content': '请问你有什么要帮助的😊'}]

for message in st.session_state['messages']:
    with st.chat_message(message['role']):
        st.markdown(message['content'])

prompt = st.chat_input('请输入')
if prompt:
    st.session_state['messages'].append({'role': 'user', 'content': prompt})
    st.chat_message('user').markdown(prompt)

    with st.spinner('😴'):
        response = get_response(st.session_state['messages'])

    st.session_state['messages'].append({'role' : 'assistant', 'content' : response})
    st.chat_message('assistant').markdown(response)













