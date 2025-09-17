"""
streamlit初体验:
    概述：
        它是python里面的一个库，可以实现python代码的网页开发

    部署格式：
        在终端中运行 streamlit run 代码地址.py 即可

"""


import streamlit as st



st.title('streamlit初体验')
# st.title('Hello World')

st.write('细雨湿衣看不见，闲花落地听无声。')

st.divider()

st.write('# 一级标题')
st.write('## 二级标题')
st.write('### 三级标题')
st.write('#### 四级标题')
st.write('##### 五级标题')
st.write('###### 六级标题')

st.divider()

st.markdown('# 一级标题')
st.markdown('## 二级标题')
st.markdown('### 三级标题')
st.markdown('#### 四级标题')
st.markdown('##### 五级标题')
st.markdown('###### 六级标题')

st.divider()

'# 一级标题'
'## 二级标题'
'### 三级标题'
'#### 四级标题'
'##### 五级标题'
'###### 六级标题'

st.divider()

st.write('一个好看的照片')
st.image('./data/OIP-C.jpg',width = 400)


