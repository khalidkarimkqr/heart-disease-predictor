import streamlit as st
import os

# Load custom CSS using os method
def local_css():
    # Construct the absolute path to the styles.css file
    css_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'styles.css')
    with open(css_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Call the function to load CSS
local_css()

# Title
st.title("About This Project")

# Description
st.write("""
This app predicts the probability of heart disease based on clinical parameters using a Logistic Regression model. 
It was built as part of an end-to-end data science project.

### Key Features:
- Trained on the Cleveland Heart Disease dataset from UCI Machine Learning Repository.
- Includes visualizations, SHAP explanations, and feature importance analysis.

### Dataset Information:
The dataset contains 14 attributes, including:
- Age, Sex, Chest Pain Type, Resting Blood Pressure, Cholesterol, etc.
- Target: 1 = Heart Disease, 0 = No Heart Disease.

### Tools Used:
- Python libraries: Pandas, Scikit-learn, Matplotlib, Seaborn, SHAP, Streamlit.
- Deployment: Streamlit Community Cloud.

For more details, check out the [GitHub repository](https://github.com/khalidkarimkqr/heart-disease-predictor).
""")

# FAQ Section
st.subheader("Frequently Asked Questions")
faq = {
    "What is this app?": "This app predicts the probability of heart disease based on clinical parameters.",
    "How accurate is the model?": "The model has an accuracy of 85% on test data.",
    "What should I do if I get a high-risk prediction?": "Consult a healthcare professional for further evaluation."
}

for question, answer in faq.items():
    with st.expander(question):
        st.write(answer)



# NEW: Acknowledgments Section
st.subheader("Acknowledgments")
st.write("""
We would like to thank the following organizations and resources for their support:

- **UCI Machine Learning Repository**: For providing the Cleveland Heart Disease dataset.
- **Streamlit Community**: For creating an amazing platform for deploying data apps.
- **Open Source Libraries**: A big thank you to the developers of Pandas, Scikit-learn, Matplotlib, Seaborn, and SHAP.
""")

# NEW: Future Improvements Section
st.subheader("Future Improvements")
st.write("""
While this app is fully functional, there are several areas where we plan to improve in the future:

- **Model Enhancements**: Experiment with more advanced models like Random Forests or Gradient Boosting.
- **Real-Time Data Integration**: Allow users to input real-time health data via wearable devices.
- **Mobile-Friendly Design**: Optimize the app for mobile devices for better accessibility.
- **Multi-Language Support**: Expand language options to reach a global audience.
- **Gamification**: Add badges and rewards for user engagement.
""")

# NEW: Interactive Feedback Form
st.subheader("Share Your Feedback")
st.write("We value your feedback! Please let us know how we can improve this app.")

rating = st.slider("Rate this app (1-5)", 1, 5)
comments = st.text_area("Comments or Suggestions")
if st.button("Submit Feedback"):
    # Save feedback to a file
    feedback_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'feedback.txt')
    with open(feedback_path, "a") as f:
        f.write(f"Rating: {rating}, Comments: {comments}\n")
    st.success("Thank you for your feedback!")
