import streamlit as st
import pandas as pd
import requests

# url = 'https://docs.google.com/spreadsheets/d/1R-17pEYYikiOUgCXypFcQIcYAIwL-hFr/edit?usp=sharing&ouid=100405249699989593907&rtpof=true&sd=true'
# r = requests.get(url)
# open('skills.xlsx', 'wb').write(r.content)
# df = pd.read_excel('skills.xlsx')




st.title('Hello World')
# # df = pd.read_csv('./skills.csv')
df = pd.read_csv('https://raw.githubusercontent.com/Germinotion/node-linker/main/skills.csv')
# https://docs.google.com/spreadsheets/d/1R-17pEYYikiOUgCXypFcQIcYAIwL-hFr/edit?usp=sharing&ouid=100405249699989593907&rtpof=true&sd=true
st.dataframe(df)

my_button = st.button('Push me!')

if my_button:
  df.label = "I've been changed!"
  df.to_csv('./skills2.csv')

  
#   https://docs.google.com/spreadsheets/d/1R-17pEYYikiOUgCXypFcQIcYAIwL-hFr/edit?usp=sharing&ouid=100405249699989593907&rtpof=true&sd=true
