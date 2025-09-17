import streamlit as st

"""
文本框: \n
    1. 普通输入框 (text_input('提示词'))：用以输入普通的文本
    2. 密码输入框 (text_input('提示词' , type = 'password'))：用以输入密码
    3. 数字输入框 (number_input())：用以输入数字，可以添加参数来规定取值范围
    4. 多行输入框 (text_area)：输入的文本可以换行
    5. 单选框    (text_radio)：让用户从多个选项中选择一个
    6. 下拉选择框 (selectbox())：让用户从下拉列表中选择一个选项
    7. 多选框    (multiselect())：让用户选择多个选项。
    8. 滑块      (slider())：让用户通过滑块选择一个数值
    9. 按钮      (button())：触发某个操作
"""

# 普通输入框
name = st.text_input('请输入你的姓名：')
if name:
    print(f'name : {name}')

# 密码输入框
pwd = st.text_input('请输入你的密码', type = 'password')
if pwd:
    print(f'pwd : {pwd}')

# 数字输入框
age = st.number_input('请输入你的年龄：', min_value = 0, max_value = 120, value = 20, step = 1)
if age:
    print(f'name : {name}')

# 多行输入框
msg = st.text_area("请输入你的留言：")
if msg:
    print(f'name : {msg}')

# 单选框
gender = st.radio('请选择你的性别', ['男', '女'])
if gender:
    print(f"选择的性别: {gender}")

# 聊天信息框
prompt = st.chat_input('请录入你的问题：')
if prompt:
    st.write(f'你的问题是：{prompt}')

# 下拉选择框
city = st.selectbox("请选择城市", ["北京", "上海", "广州", "深圳"])
if city:
    print(f"选择的城市: {city}")


# 多选框
hobbies = st.multiselect("请选择你的爱好", ["阅读", "运动", "音乐", "编程"])
if hobbies:
    print(f"选择的爱好: {hobbies}")


# 滑块
rating = st.slider("请评分（1-5）", min_value=1, max_value=5, value=3)
if rating:
    print(f"评分: {rating}")


# 按钮
if st.button("点击我"):
    st.write("按钮被点击了！")



# 角色信息框

# 1. with st.chat_message()
with st.chat_message('user'):
    st.write('hello 😘😘😘😘')


# 2. 变量名 = st.chat_message()
msg = st.chat_message('assistant')
msg.write('你好，人类')
