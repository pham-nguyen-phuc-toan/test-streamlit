import streamlit as st
import tensorflow
import torch
import transformers
import openai
import requests

st.title('Code generation')

prompt = st.text_area('Input code to complete', '')

max_length = st.slider('Maximum length', 1, 200, 1, 1, key=1)

num_completions = st.slider('Number of completions', 1, 10, 1, 1, key=2)

if st.button('Submit'):
    headers = {
        'accept': 'application/json',
        'content-type': 'application/x-www-form-urlencoded',
    }
    
    params = {
        "prompt": prompt,
        "max_length": max_length,
        "num_completions": num_completions
    }
    
    response = requests.post("https://6e0b-116-102-221-147.ngrok-free.app/chatgpt", headers=headers, params=params)
    
    if response.status_code != 500:
        response = response.json()    
        result = response['result']
        st.write('Generated code')
        st.code(result)
    else:
        st.write('No solutions!')
