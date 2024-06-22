import streamlit as st
import pandas as pd
import time
st.title("Indian Startup") # to add title to the website
st.subheader("I am learing streamlit") # adding subheader

st.subheader("and i am loving it")
st.write("hi my name is syed mansoor shafi and this is a normal text")
st.markdown("""
### My favourite movies
- Race 3
- Humshakals
- Dabangg""")
st.code('''
def foo():
   return foo** 2
x = foo(2)''')
st.latex('A^2 + B ^ 3 = 2^ A.B')
d = pd.DataFrame({
    'name':'syed mansoor',
    'age':23,
    'gender':'male'
},index = [1,2,3])
st.dataframe(d)
st.metric('REvenue','Rs 3L','3%')

# df = pd.DataFrame({'name':'syed mansoor shafi',
#     'subjects':{'english':[34,45,56,67,78],
#                'math':[56,67,78,89,90],
#                'science':[34,45,56,67,8]}})

# st.json(df)
st.sidebar.title('sidebar title')
col1,col2 = st.columns(2)
with col1:
    st.write('col1')
with col2:
    st.write('col2')
st.error('Login failed')
st.success('success')
st.warning('warning')
st.info('info')
# bar = st.progress(0)
# for i in range(1,101):
#     time.sleep(0.1)
#     bar.progress(i)
# email = st.text_input('Enter your email  = ')
# # print(f'{email :}')
# number =st.number_input('enter number = ')
# date = st.date_input('enter date = ')
# if email == 'saeedmansoor56@gmail.com':
#     password = st.number_input('enter password = ')
#     st.balloons()
# password = st.text_input('enter password = ')
# btn = st.button('Do Login')
# if btn:
#     if email == 'saeedmansoor56@gmail.com' and password == '1234':
    
    #     st.success('success')
    # elif email == 'saeedmansoor56@gmail.com' and password != '1234':
    #     st.warning('Wrong Password')
    #     password = st.text_input('Enter password = ')
    #     if password == '1234':
    #         st.success('DONE')
    #         st.balloons()
    #     else:
    #         st.warning('Account locked')
    # else:
    #     st.error("error")

gender = st.selectbox('Select Box',['Male','Female','Others'])