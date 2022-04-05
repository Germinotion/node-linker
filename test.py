import streamlit as st
import pandas as pd
import requests
from itertools import combinations

st.title('Hello World')
df = pd.read_csv('https://raw.githubusercontent.com/Germinotion/node-linker/main/skills.csv')
# st.dataframe(df)
names = df.name
combinations_df = pd.DataFrame (list(combinations(names, 2)))
combinations_df['y/n'] = ''
combinations_df['skip?'] = ''

st.dataframe(combinations_df)

for i in range(len(combinations_df[0][:10])):
    if len(combinations_df['y/n'][i]) < 1 and len(combinations_df['skip?'][i]) < 1:
        st.write(f"Is {combinations_df[0][i]} related to {combinations_df[1][i]}?")
#         y = st.radio('Pick one', ['yes', 'no','skip'])
#         y = st.text_input('y/n/skip')
#         if y == 'y' or y == 'yes':
#             combinations_df['y/n'][i] = 'y'
#         elif y == 'n' or y == 'no':
#             combinations_df['y/n'][i] = 'n'
#         elif y == 's' or y == 'skip':
#             combinations_df['skip?'][i] = 'y'
    else:
        continue



# my_button = st.button('Push me!')

# if my_button:
#   df.label = "I've been changed!"
#   df.to_csv('./skills2.csv')

  
#   https://docs.google.com/spreadsheets/d/1R-17pEYYikiOUgCXypFcQIcYAIwL-hFr/edit?usp=sharing&ouid=100405249699989593907&rtpof=true&sd=true
