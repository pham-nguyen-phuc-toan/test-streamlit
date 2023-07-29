# import streamlit as st
# import tensorflow
# import torch
# import transformers
# import openai

# lang=st.selectbox("Select the Language of  the Solution:", ("Python", "C++", "Java"))
# question=st.text_area("Input the Question Here")
# button=st.button("Generate")

# def response1(ques):
#     openai.api_key=st.secrets["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"]
    
#     response = openai.Completion.create(
#         model="code-cushman-001",
#         prompt=f""""Give a {lang} solution for the Leetcode question 
#                     Leetcode Question: {question}
#                     {lang} Solution: """,
#         temperature=0,
#         max_tokens=1111,
#         top_p=1,
#         frequency_penalty=0,
#         presence_penalty=0
#         )
#     print(response)
#     return response.choices[0].text

# if question and button:
#     answer=response1(question)
#     st.code(answer)

# # from transformers import BertConfig, BertModel

# # model = transformers.BertModel.from_pretrained("bert-base-uncased")
# # st.write(model)

# # pipe = transformers.pipeline("text-classification")

# # st.write(pipe("This restaurant is awesome"))

# st.title('Playground')

# txt = st.text_area('Input prompt', '')

# st.button('Submit')

# temp = st.slider('Temperature', 0.00, 2.00, 1.00, 0.01, key=1)

# top_p = st.slider('Top P', 0.00, 1.00, 1.00, 0.01, key=2)
    
# max_len = st.slider('Maximum length', 1, 4000, 1, 1, key=3)

# st.checkbox('Show probabilities')

# code = '''print('Hello world')'''
# st.code(code, language='python')

import streamlit as st

st.title("Random Words Generator")
st.header("Random Word")
random_word = st.subheader("-")
word_meaning = st.text("Meaning: -")
st.write("Click the `Generate` button to generate new word")
st.button("Generate")
