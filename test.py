import streamlit as st
import pandas as pd
import requests
from itertools import combinations

st.title('Hello World')
df = pd.read_csv('https://raw.githubusercontent.com/Germinotion/node-linker/main/skills.csv')
# st.dataframe(df)

combinations_df = pd.DataFrame (list(combinations(names, 2)))
combinations_df['y/n'] = ''
combinations_df['skip?'] = ''

st.dataframe(combinations_df)

my_button = st.button('Push me!')

if my_button:
  df.label = "I've been changed!"
  df.to_csv('./skills2.csv')

  
#   https://docs.google.com/spreadsheets/d/1R-17pEYYikiOUgCXypFcQIcYAIwL-hFr/edit?usp=sharing&ouid=100405249699989593907&rtpof=true&sd=true
