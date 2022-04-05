import streamlit as st
import pandas as pd



st.title('Hello World')
df = pd.read_excel('https://github.com/Germinotion/node-linker/blob/main/skills.xlsx')

st.dataframe(df)
