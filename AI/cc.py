import streamlit as st
from cd import get

st.title('聊天')

st.divider()

if 'messages' not in st.session_state:
    st.session_state['messages'] = [{'role' : 'assistant', 'content' : '请问有什么可以帮你的吗？'}]

for message in st.session_state['messages']:
    st.chat_message(message['role']).markdown(message['content'])

prompt = st.chat_input("请输入你的问题")

if prompt:
    st.session_state['messages'].append({'role' : 'user', 'content' : prompt})
    st.chat_message('user').markdown(prompt)

    with st.spinner('思考中...'):
        response = get(st.session_state['messages'])

    st.session_state['messages'].append({'role' : 'assistant', 'content' : response})
    st.chat_message('assistant').markdown(response)


