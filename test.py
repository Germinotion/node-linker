import streamlit as st
import pandas as pd



st.title('Hello World')
df = pd.read_csv('https://github.com/Germinotion/node-linker/blob/main/skills.csv')

st.dataframe(df)
