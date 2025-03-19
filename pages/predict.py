import streamlit as st
import pandas as pd
import pickle
import matplotlib.pyplot as plt
import shap
import time
import os

# Load custom CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

CSS_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'styles.css')
local_css(CSS_PATH)

# Load the Logistic Regression model
MODEL_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'heart_disease_model.pkl')
with open(MODEL_PATH, 'rb') as f:
    clf = pickle.load(f)

# Load dataset for feature importance
DATA_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'heart-disease.csv')
df = pd.read_csv(DATA_PATH)
X = df.drop('target', axis=1)

# Initialize session state for inputs and prediction (empty by default)
if "age" not in st.session_state:
    st.session_state.age = None
if "sex" not in st.session_state:
    st.session_state.sex = None
if "cp" not in st.session_state:
    st.session_state.cp = None
if "trestbps" not in st.session_state:
    st.session_state.trestbps = None
if "chol" not in st.session_state:
    st.session_state.chol = None
if "fbs" not in st.session_state:
    st.session_state.fbs = None
if "restecg" not in st.session_state:
    st.session_state.restecg = None
if "thalach" not in st.session_state:
    st.session_state.thalach = None
if "exang" not in st.session_state:
    st.session_state.exang = None
if "oldpeak" not in st.session_state:
    st.session_state.oldpeak = None
if "slope" not in st.session_state:
    st.session_state.slope = None
if "ca" not in st.session_state:
    st.session_state.ca = None
if "thal" not in st.session_state:
    st.session_state.thal = None
if "prediction" not in st.session_state:
    st.session_state.prediction = None
if "risk_level" not in st.session_state:
    st.session_state.risk_level = None

# Title
st.title("Predict Heart Disease")

# User inputs
st.subheader("Enter Your Medical Attributes")
st.session_state.age = st.number_input("Age", min_value=0, max_value=120, value=st.session_state.age or 0)

# Sex (default is "Choose an Option")
sex_options = {"Male (1)": 1, "Female (0)": 0}
sex_placeholder = "Choose an Option"
st.session_state.sex = st.selectbox(
    "Sex",
    [sex_placeholder] + list(sex_options.keys()),
    index=0 if st.session_state.sex == sex_placeholder else list(sex_options.keys()).index(st.session_state.sex) + 1 if st.session_state.sex in sex_options else 0
)

# Chest Pain Type (cp)
cp_options = {
    "Typical Angina (0)": 0,
    "Atypical Angina (1)": 1,
    "Non-Anginal Pain (2)": 2,
    "Asymptomatic (3)": 3
}
cp_placeholder = "Choose an Option"
st.session_state.cp = st.selectbox(
    "Chest Pain Type",
    [cp_placeholder] + list(cp_options.keys()),
    index=0 if st.session_state.cp == cp_placeholder else list(cp_options.keys()).index(st.session_state.cp) + 1 if st.session_state.cp in cp_options else 0
)

st.session_state.trestbps = st.number_input("Resting Blood Pressure (mm Hg)", min_value=0, max_value=250, value=st.session_state.trestbps or 0)
st.session_state.chol = st.number_input("Cholesterol (mg/dL)", min_value=0, max_value=600, value=st.session_state.chol or 0)

# Fasting Blood Sugar (fbs)
fbs_options = {"No (0)": 0, "Yes (1)": 1}
fbs_placeholder = "Choose an Option"
st.session_state.fbs = st.selectbox(
    "Fasting Blood Sugar > 120 mg/dL",
    [fbs_placeholder] + list(fbs_options.keys()),
    index=0 if st.session_state.fbs == fbs_placeholder else list(fbs_options.keys()).index(st.session_state.fbs) + 1 if st.session_state.fbs in fbs_options else 0
)

# Resting ECG (restecg)
restecg_options = {
    "Normal (0)": 0,
    "ST-T Wave Abnormality (1)": 1,
    "Left Ventricular Hypertrophy (2)": 2
}
restecg_placeholder = "Choose an Option"
st.session_state.restecg = st.selectbox(
    "Resting ECG Results",
    [restecg_placeholder] + list(restecg_options.keys()),
    index=0 if st.session_state.restecg == restecg_placeholder else list(restecg_options.keys()).index(st.session_state.restecg) + 1 if st.session_state.restecg in restecg_options else 0
)

st.session_state.thalach = st.number_input("Maximum Heart Rate Achieved", min_value=0, max_value=250, value=st.session_state.thalach or 0)

# Exercise Induced Angina (exang)
exang_options = {"No (0)": 0, "Yes (1)": 1}
exang_placeholder = "Choose an Option"
st.session_state.exang = st.selectbox(
    "Exercise Induced Angina",
    [exang_placeholder] + list(exang_options.keys()),
    index=0 if st.session_state.exang == exang_placeholder else list(exang_options.keys()).index(st.session_state.exang) + 1 if st.session_state.exang in exang_options else 0
)

st.session_state.oldpeak = st.number_input("ST Depression Induced by Exercise", min_value=0.0, max_value=10.0, value=st.session_state.oldpeak or 0.0)

# Slope of Peak Exercise ST Segment (slope)
slope_options = {
    "Upsloping (0)": 0,
    "Flat (1)": 1,
    "Downsloping (2)": 2
}
slope_placeholder = "Choose an Option"
st.session_state.slope = st.selectbox(
    "Slope of Peak Exercise ST Segment",
    [slope_placeholder] + list(slope_options.keys()),
    index=0 if st.session_state.slope == slope_placeholder else list(slope_options.keys()).index(st.session_state.slope) + 1 if st.session_state.slope in slope_options else 0
)

st.session_state.ca = st.number_input("Number of Major Vessels Colored by Fluoroscopy", min_value=0, max_value=4, value=st.session_state.ca or 0)

# Thalassemia (thal)
thal_options = {
    "Normal (0)": 0,
    "Fixed Defect (1)": 1,
    "Reversible Defect (2)": 2
}
thal_placeholder = "Choose an Option"
st.session_state.thal = st.selectbox(
    "Thalassemia",
    [thal_placeholder] + list(thal_options.keys()),
    index=0 if st.session_state.thal == thal_placeholder else list(thal_options.keys()).index(st.session_state.thal) + 1 if st.session_state.thal in thal_options else 0
)

# Predict button
if st.button("Predict"):
    # Input validation
    if (
        st.session_state.age is None or st.session_state.age <= 0 or
        st.session_state.sex == sex_placeholder or
        st.session_state.cp == cp_placeholder or
        st.session_state.trestbps is None or st.session_state.trestbps <= 0 or
        st.session_state.chol is None or st.session_state.chol <= 0 or
        st.session_state.fbs == fbs_placeholder or
        st.session_state.restecg == restecg_placeholder or
        st.session_state.thalach is None or st.session_state.thalach <= 0 or
        st.session_state.exang == exang_placeholder or
        st.session_state.oldpeak is None or
        st.session_state.slope == slope_placeholder or
        st.session_state.ca is None or
        st.session_state.thal == thal_placeholder
    ):
        st.error("Please enter valid values for all fields.")
    else:
        # Show progress bar
        progress_bar = st.progress(0)
        for i in range(100):
            time.sleep(0.02)
            progress_bar.progress(i + 1)

        # Prepare input data
        input_data = pd.DataFrame({
            'age': [st.session_state.age],
            'sex': [sex_options[st.session_state.sex]],
            'cp': [cp_options[st.session_state.cp]],
            'trestbps': [st.session_state.trestbps],
            'chol': [st.session_state.chol],
            'fbs': [fbs_options[st.session_state.fbs]],
            'restecg': [restecg_options[st.session_state.restecg]],
            'thalach': [st.session_state.thalach],
            'exang': [exang_options[st.session_state.exang]],
            'oldpeak': [st.session_state.oldpeak],
            'slope': [slope_options[st.session_state.slope]],
            'ca': [st.session_state.ca],
            'thal': [thal_options[st.session_state.thal]]
        })

        # Make prediction
        prediction = clf.predict_proba(input_data)[0][1] * 100
        st.session_state.prediction = prediction

        # Risk level indicator
        if prediction < 30:
            st.session_state.risk_level = "Low Risk"
            color = "green"
        elif prediction < 70:
            st.session_state.risk_level = "Medium Risk"
            color = "orange"
        else:
            st.session_state.risk_level = "High Risk"
            color = "red"

        st.subheader("Prediction Result")
        st.write(f"Probability of Heart Disease: {prediction:.2f}%")
        st.markdown(f"<h3 style='color:{color};'>{st.session_state.risk_level}</h3>", unsafe_allow_html=True)

        # SHAP Explanation
        explainer = shap.Explainer(clf, X)
        shap_values = explainer(input_data)
        st.subheader("Prediction Explanation")
        fig, ax = plt.subplots()
        shap.plots.waterfall(shap_values[0], show=False)
        st.pyplot(fig)

                # Feature Importance
        if hasattr(clf, 'coef_'):  # For Logistic Regression
            importances = clf.coef_[0]

        importance_df = pd.DataFrame({'Feature': X.columns, 'Importance': importances})
        importance_df = importance_df.sort_values(by='Importance', ascending=False)

        st.subheader("Feature Importance")
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.barh(importance_df['Feature'], importance_df['Importance'], color='skyblue')
        ax.set_title('Feature Importance')
        ax.invert_yaxis()
        st.pyplot(fig)

        # Download button
        result_df = pd.DataFrame({
            "Feature": input_data.columns,
            "Value": [
                st.session_state.age,
                st.session_state.sex.split(" ")[0] if st.session_state.sex != sex_placeholder else None,
                st.session_state.cp.split(" ")[0] if st.session_state.cp != cp_placeholder else None,
                st.session_state.trestbps,
                st.session_state.chol,
                st.session_state.fbs.split(" ")[0] if st.session_state.fbs != fbs_placeholder else None,
                st.session_state.restecg.split(" ")[0] if st.session_state.restecg != restecg_placeholder else None,
                st.session_state.thalach,
                st.session_state.exang.split(" ")[0] if st.session_state.exang != exang_placeholder else None,
                st.session_state.oldpeak,
                st.session_state.slope.split(" ")[0] if st.session_state.slope != slope_placeholder else None,
                st.session_state.ca,
                st.session_state.thal.split(" ")[0] if st.session_state.thal != thal_placeholder else None
            ],
            "Prediction": [f"{prediction:.2f}%"] * len(input_data.columns)
        })
        st.download_button(
            label="Download Results",
            data=result_df.to_csv(index=False),
            file_name="prediction_results.csv",
            mime="text/csv"
        )

        # Risk Factor Analysis
        st.subheader("Risk Factor Analysis")
        if st.session_state.chol > 200:
            st.warning("Your cholesterol level is high. Consider consulting a doctor.")
        if st.session_state.trestbps > 140:
            st.warning("Your resting blood pressure is elevated. Monitor it regularly.")
        if st.session_state.age > 50:
            st.info("Age is a significant risk factor. Stay proactive about your health.")

        # Health Tips
        st.subheader("Health Tips")
        if prediction > 50:
            st.warning("You are at high risk. Here are some tips:")
            st.write("- Reduce sodium intake to lower blood pressure.")
            st.write("- Exercise for at least 30 minutes daily.")
        else:
            st.info("You are at low risk. Keep up the good work!")
            st.write("- Maintain a balanced diet.")
            st.write("- Schedule regular health check-ups.")

        # Comparison Tool
        st.subheader("Compare with Averages")
        average_values = df.mean(numeric_only=True)
        comparison = pd.DataFrame({
            "Your Input": [
                st.session_state.age,
                st.session_state.sex.split(" ")[0] if st.session_state.sex != sex_placeholder else None,
                cp_options.get(st.session_state.cp.split(" ")[0], None) if st.session_state.cp != cp_placeholder else None,
                st.session_state.trestbps,
                st.session_state.chol,
                fbs_options.get(st.session_state.fbs.split(" ")[0], None) if st.session_state.fbs != fbs_placeholder else None,
                restecg_options.get(st.session_state.restecg.split(" ")[0], None) if st.session_state.restecg != restecg_placeholder else None,
                st.session_state.thalach,
                exang_options.get(st.session_state.exang.split(" ")[0], None) if st.session_state.exang != exang_placeholder else None,
                st.session_state.oldpeak,
                slope_options.get(st.session_state.slope.split(" ")[0], None) if st.session_state.slope != slope_placeholder else None,
                st.session_state.ca,
                thal_options.get(st.session_state.thal.split(" ")[0], None) if st.session_state.thal != thal_placeholder else None
            ],
            "Average": average_values
        }).dropna()
        st.table(comparison)

# Display saved prediction and risk level
if st.session_state.prediction is not None:
    st.subheader("Last Prediction Result")
    st.write(f"Probability of Heart Disease: {st.session_state.prediction:.2f}%")
    st.markdown(f"<h3 style='color:green;'>{st.session_state.risk_level}</h3>", unsafe_allow_html=True)