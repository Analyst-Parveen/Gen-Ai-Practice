from model_loder import model
import streamlit as st


st.header('Research Tool')
user_input=st.text_input('enter you input')

if st.button('summarize'):
    result=model.invoke(user_input)
    st.write(result.content)