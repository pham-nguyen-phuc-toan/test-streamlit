import streamlit as st
import numpy
import matplotlib
import sklearn
import transformers


pipe = transformers.pipeline("text-classification")

st.write(pipe("This restaurant is awesome"))

st.title('Playground')

txt = st.text_area('Input prompt', '')



st.button('Submit')

temp = st.slider('Temperature', 0.00, 2.00, 1.00, 0.01, key=1)

top_p = st.slider('Top P', 0.00, 1.00, 1.00, 0.01, key=2)
    
max_len = st.slider('Maximum length', 1, 4000, 1, 1, key=3)

st.checkbox('Show probabilities')

code = '''print('Hello world')'''
st.code(code, language='python')

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

plt.plot(xpoints, ypoints)
plt.show()
