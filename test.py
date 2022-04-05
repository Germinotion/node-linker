import streamlit as st
import pandas as pd



st.title('Hello World')
df = pd.read_csv('./skills.csv')

st.dataframe(df)

my_button = st.button('Push me!')

if my_button:
  df.label = "I've been changed!"
  df.to_csv('./skills2.csv')
