import pandas as pd
import streamlit as st

st.write('静态表格之 **字典 + 列表**')
st.table({
    'name' : ['A', 'B', 'C'],
    'age' : [18 , 16 , 19],
    'gender' : ['man' , 'man' , 'man']
})

st.divider()

st.markdown('静态表格之 **dataFrame对象**')
df = pd.DataFrame({
    'name' : ['A', 'B', 'C'],
    'age' : [18 , 16 , 19],
    'gender' : ['man' , 'man' , 'man']
})
st.dataframe(df)

st.divider()





















