import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# Page config
st.set_page_config(page_title="Spam Classifier", page_icon="📧", layout="centered")

# Custom CSS (Design 🔥)
st.markdown("""
    <style>
    body {
        background-color: #0e1117;
    }
    .main {
        background-color: #0e1117;
    }
    .title {
        text-align: center;
        font-size: 40px;
        color: #00ffcc;
        font-weight: bold;
    }
    .subtitle {
        text-align: center;
        color: #cccccc;
        margin-bottom: 20px;
    }
    .stTextArea textarea {
        border-radius: 10px;
        border: 2px solid #00ffcc;
    }
    .stButton>button {
        background-color: #00ffcc;
        color: black;
        border-radius: 10px;
        font-size: 16px;
        padding: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="title">📧 Spam Classifier</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Detect whether a message is Spam or Not</div>', unsafe_allow_html=True)

# Load dataset
df = pd.read_csv("spam.csv", sep='\t', names=['label', 'message'])

# Convert labels
df['label'] = df['label'].map({'ham': 0, 'spam': 1})

# Train model
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(df['message'])
y = df['label']

model = MultinomialNB()
model.fit(X, y)

# Input
user_input = st.text_area("✉ Enter your message:")

# Predict
if st.button("🚀 Predict"):
    if user_input.strip() != "":
        input_vec = vectorizer.transform([user_input])
        result = model.predict(input_vec)

        if result[0] == 1:
            st.markdown("<h3 style='color:red; text-align:center;'>🚨 SPAM MESSAGE</h3>", unsafe_allow_html=True)
        else:
            st.markdown("<h3 style='color:green; text-align:center;'>✅ NOT SPAM</h3>", unsafe_allow_html=True)
    else:
        st.warning("⚠ Please enter a message")

# Footer
st.markdown("---")
st.markdown("<p style='text-align:center; color:gray;'>Built with ❤️ using Streamlit</p>", unsafe_allow_html=True)