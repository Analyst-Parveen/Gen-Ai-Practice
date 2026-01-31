from model_loder import model
import streamlit as st
from langchain_core.prompts import PromptTemplate,load_prompt
st.header('Research Tool')
paper_input=st.selectbox('select research paper',['attention is all you need','BERT:pretraining of Deep bidrectional Transformer','GPT3:language models are Few sort learners','Diffusion model beat GANs on image synthesis'])
style_input=st.selectbox('select explanation style',['Begineer Friendly','Technical','code-oriented','mathmatical'])
length_input=st.selectbox('select explanation length',['short(1-2 paragraph)','medium(3-5paragraph)','long(detailed-explanation)'])



template=load_prompt('template.json')
prompt=template.invoke({
    'paper_input':paper_input,
    'style_input':style_input,
    'length_input':length_input
})


if st.button('summarize'):
    result=model.invoke(prompt)
    st.write(result.content)