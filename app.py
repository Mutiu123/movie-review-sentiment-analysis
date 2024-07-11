import pandas as pd 
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle as pk

# Load model and scaler
model = pk.load(open('model/MRSAmodel.pkl','rb'))
scaler = pk.load(open('model/scaler.pkl','rb'))

# Title
st.markdown('## Sentiment Analysis Tool')

# User input for review
review = st.text_input('**Please Enter Your Review**', '')

# Button to predict sentiment
if st.button('**Click to Predict**'):
    # Scale review text
    review_scale = scaler.transform([review]).toarray()
    # Predict sentiment
    result = model.predict(review_scale)
    
    # Display result with styling
    if result[0] == 0:
        st.markdown('**Result:** Negative Review 😞', unsafe_allow_html=True)
    else:
        st.markdown('**Result:** Positive Review 😊', unsafe_allow_html=True)
