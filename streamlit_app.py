import streamlit as st
import os

# Load custom CSS
def local_css():
    css_path = os.path.join(os.path.dirname(__file__), 'styles.css')
    with open(css_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Load Google Fonts
def load_fonts():
    st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Nexa:wght@700&display=swap" rel="stylesheet">
    """, unsafe_allow_html=True)

# Call CSS and Fonts
local_css()
load_fonts()

# Landing Page
st.title("❤️ Heart Disease Prediction")
st.write("""
Welcome to the Heart Disease Prediction App! This application uses machine learning to predict the probability of heart disease based on clinical parameters.

### How It Works:
1. Click the "Predict Now" button below.
2. Enter your medical attributes to get a prediction.
3. Explore visualizations and explanations to understand the results better.
""")

if st.button("Predict Now"):
    st.switch_page("pages/predict.py")

# About Section Prompt and Button
st.write("Click on the button below to learn more about the app:")
if st.button("About This App"):
    st.switch_page("pages/about.py")  # Navigate to the About page

# Footer
st.markdown("---")
st.markdown("Made with ❤️ by Khalid")