# ❤️ Heart Disease Predictor App

![Streamlit App](https://github.com/khalidkarimkqr/heart-disease-predictor/blob/main/images/app_screenshot.png)  
*Screenshot of the Heart Disease Prediction App*

---

## 📌 Table of Contents

1. [What is this App?](#what-is-this-app)
2. [Why is this App Useful?](#why-is-this-app-useful)
3. [How Does It Work?](#how-does-it-work)
4. [Model Training and Data Analysis](#model-training-and-data-analysis)
5. [Features](#features)
6. [How to Run Locally](#how-to-run-locally)
7. [Screenshots](#screenshots)
8. [Jupyter Notebook](#jupyter-notebook)
9. [Contributing](#contributing)
10. [License](#license)

---

## 💡 What is this App?

The **Heart Disease Predictor App** is a machine learning-powered tool that predicts the probability of heart disease based on clinical parameters such as age, sex, cholesterol levels, blood pressure, and more. The app uses a Logistic Regression model trained on the **Heart Disease Dataset** from the UCI Machine Learning Repository.

This app is designed to:
- Provide personalized risk assessments.
- Explain predictions using SHAP values.
- Visualize feature importance.
- Offer actionable health tips based on the user's risk level.

---

## 🌟 Why is this App Useful?

Heart disease is one of the leading causes of death worldwide. Early detection and risk assessment can significantly improve outcomes. This app helps users:
- Assess their risk of heart disease in minutes.
- Understand which factors contribute most to their risk.
- Get actionable advice to improve their health.

It is intended for educational purposes and should not replace professional medical advice.

---

## 🔧 How Does It Work?

The app uses a pre-trained Logistic Regression model to predict the probability of heart disease. Here’s how it works:
1. Users input their medical attributes (e.g., age, cholesterol, blood pressure).
2. The app processes the inputs and calculates the probability of heart disease.
3. Results are displayed with:
   - A risk level (Low, Medium, High).
   - SHAP explanations to show feature contributions.
   - Feature importance visualization.
   - Health tips and gamification badges.

---

## 🧠 Model Training and Data Analysis

### Overview
The model was trained using the **Heart Disease Dataset** from the UCI Machine Learning Repository. Below is a summary of the steps I followed to build the model:

1. **Data Cleaning**:
   - Handled missing values and removed duplicates.
   - Encoded categorical variables (e.g., `sex`, `cp`, `thal`) into numerical values.

2. **Exploratory Data Analysis (EDA)**:
   - Analyzed distributions of key features like `age`, `chol`, and `trestbps`.
   - Visualized correlations between features using heatmaps and pair plots.

3. **Feature Selection**:
   - Used statistical methods (e.g., correlation matrix, feature importance from Random Forest) to identify the most impactful features.
   - Selected features like `age`, `sex`, `cp`, `trestbps`, `chol`, `thalach`, and `oldpeak`.

4. **Model Training**:
   - Trained a Logistic Regression model due to its simplicity and interpretability.
   - Split the dataset into training and testing sets (80% train, 20% test).
   - Achieved an accuracy of **85%** and an F1-score of **86%**.

5. **Evaluation**:
   - Evaluated the model using metrics like accuracy, precision, recall, and ROC-AUC.
   - Used SHAP values to explain the model’s predictions.

6. **Deployment**:
   - Saved the trained model as `heart_disease_model.pkl` using `pickle`.
   - Integrated the model into the Streamlit app for real-time predictions.

### Dive Deeper: Jupyter Notebook
For a detailed walkthrough of the entire process, including code, visualizations, and markdown explanations, check out the accompanying **Jupyter Notebook**: [`heart_disease_analysis.ipynb`](https://github.com/khalidkarimkqr/heart-disease-predictor/blob/main/end-to-end-heart-disease-classification.ipynb).

---

## 🛠 Features

- **Prediction**: Enter medical attributes to get a personalized risk assessment.
- **SHAP Explanations**: Understand which features contribute most to your prediction.
- **Feature Importance**: Visualize the importance of each feature in the model.
- **Health Tips**: Get actionable advice based on your risk level.
- **Gamification**: Earn badges for low, medium, or high-risk predictions.
- **About Page**: Learn more about the app, dataset, and model.

---

## 🚀 How to Run Locally

If you want to run this app on your local machine, follow these steps:

### Prerequisites

- Python 3.8 or higher
- Git installed on your system
- Basic knowledge of Python and Streamlit

### Step 1: Clone the Repository

```bash
git clone https://github.com/khalidkarimkqr/heart-disease-predictor.git
cd heart-disease-predictor
```

### Step 2: Install Dependencies

```bash
# Install dependencies
pip install -r requirements.txt

# If you encounter issues, upgrade pip:
pip install --upgrade pip
```

### Step 3: Run the App
```bash
# Run the app
streamlit run streamlit_app.py
```

