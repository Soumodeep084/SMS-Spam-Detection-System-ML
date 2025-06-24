import streamlit as st
import joblib

# Load the trained SMS Spam Classifier Model (Pipeline with Vectorizer + TFIDF + Classifier)
model = joblib.load('spam_model.pkl')  # Change this if your file name differs

# Streamlit App Configuration
st.set_page_config(page_title="SMS Spam Classifier", page_icon="📱", layout="centered")

# Custom Styling
st.markdown(
    """
     <style>
        .block-container {
            padding-top: 0rem;
            padding-bottom: 0rem;
        }
        .css-z5fcl4 {
            padding-top: 0rem;
            padding-bottom: 0rem;
        }
        header {visibility: hidden;}
        .css-1vq4p4l {padding: 0rem;}
    </style>
    """, unsafe_allow_html=True)

# App Title
st.title("📱 SMS Spam Detection App")
st.markdown("### Enter an SMS message below to check whether it's **SPAM** or **HAM (Not Spam)**.")

# User Input
user_input = st.text_area("SMS Text Here:", height=150, placeholder="Type or paste SMS content...")

# Buttons
predict_btn = st.button("Predict")
clear_btn = st.button("Clear")

if predict_btn:
    if user_input.strip() == "":
        st.warning("Please enter some SMS text.")
    else:
        # Predict (No manual preprocessing required as your pipeline handles it)
        prediction = model.predict([user_input])[0]

        if prediction == 1:
            st.error("🚨 This SMS is classified as **SPAM**.")
            st.markdown("#### ❌ Beware! This message might be unwanted or fraudulent.")
        else:
            st.success("✅ This SMS is **Not Spam**.")
            st.markdown("#### 📩 This message seems safe and normal.")

if clear_btn:
    st.rerun()
