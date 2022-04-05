import streamlit as st
import pandas as pd



st.title('Hello World')
df = pd.read_csv('./skills.csv')

st.dataframe(df)
