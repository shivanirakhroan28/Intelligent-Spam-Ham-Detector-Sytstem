
import string
import streamlit as st
import pickle

feature_extraction = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

st.markdown(
    """
    <style>
    .stApp {
        background-color: black;
        color:#F9B572;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <style>
    textarea {
        background-color: yellow; 
        color: #fff; /* Change text color *  #f0f8ff;/
        font-size: 16px;
        border: 2px solid #4CAF50;
        border-radius: 10px; 
        padding: 10px; 
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("📧 Email/SMS Spam Classifier")

input_sms = st.text_area("Enter the message")

# Function to preprocess and transform the text
def transform_text(text):
    text = text.lower()
    text = ''.join([char for char in text if char not in string.punctuation])
    return text

if st.button('Predict'):
    if input_sms.strip():
        # Preprocess the input text
        transformed_sms = transform_text(input_sms)
        # Transform using the pre-trained vectorizer
        vector_input = feature_extraction.transform([transformed_sms])
        # Make the prediction
        prediction = model.predict(vector_input)[0]
        # Display the result
        if prediction == 1:
            st.success(" 🟢 The message is classified as: **Ham (Not Spam)**")
        else:
            st.error("🔴 The message is classified as: **Spam**")
    else:
        st.warning("⚠️ Please enter a valid message to classify.")
