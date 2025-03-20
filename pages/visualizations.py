import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Replace this path with the actual path to your file
DATA_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'heart-disease.csv')
df = pd.read_csv(DATA_PATH)

# Title
st.title("Dataset Insights and Visualizations")

# Dataset preview
st.subheader("Dataset Preview")
st.write(df.head())

# Summary statistics
st.subheader("Summary Statistics")
st.write(df.describe())

# Correlation heatmap
st.subheader("Correlation Heatmap")
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
st.pyplot(plt)

# Age distribution
st.subheader("Age Distribution")
plt.figure(figsize=(8, 6))
sns.histplot(df['age'], kde=True, bins=20, color='green')
plt.title("Age Distribution")
st.pyplot(plt)

# Target distribution
st.subheader("Target Distribution")
plt.figure(figsize=(8, 6))
sns.countplot(x='target', data=df, palette='Set2')
plt.title("Heart Disease vs No Heart Disease")
st.pyplot(plt)

# NEW: Gender Distribution by Target
st.subheader("Gender Distribution by Heart Disease")
plt.figure(figsize=(8, 6))
sns.countplot(x='sex', hue='target', data=df, palette='Set1')
plt.title("Gender Distribution (0 = Female, 1 = Male)")
plt.xlabel("Sex (0 = Female, 1 = Male)")
plt.ylabel("Count")
st.pyplot(plt)

# NEW: Chest Pain Type Distribution
st.subheader("Chest Pain Type Distribution")
plt.figure(figsize=(8, 6))
sns.countplot(x='cp', hue='target', data=df, palette='viridis')
plt.title("Chest Pain Types by Heart Disease")
plt.xlabel("Chest Pain Type (0-3)")
plt.ylabel("Count")
st.pyplot(plt)

# NEW: Resting Blood Pressure vs Age
st.subheader("Resting Blood Pressure vs Age")
plt.figure(figsize=(8, 6))
sns.scatterplot(x='age', y='trestbps', hue='target', data=df, palette='coolwarm')
plt.title("Resting Blood Pressure vs Age")
plt.xlabel("Age")
plt.ylabel("Resting Blood Pressure (mm Hg)")
st.pyplot(plt)

# NEW: Cholesterol Levels vs Age
st.subheader("Cholesterol Levels vs Age")
plt.figure(figsize=(8, 6))
sns.scatterplot(x='age', y='chol', hue='target', data=df, palette='magma')
plt.title("Cholesterol Levels vs Age")
plt.xlabel("Age")
plt.ylabel("Cholesterol (mg/dL)")
st.pyplot(plt)

# NEW: Maximum Heart Rate Achieved by Age
st.subheader("Maximum Heart Rate Achieved by Age")
plt.figure(figsize=(8, 6))
sns.scatterplot(x='age', y='thalach', hue='target', data=df, palette='plasma')
plt.title("Maximum Heart Rate Achieved by Age")
plt.xlabel("Age")
plt.ylabel("Maximum Heart Rate Achieved")
st.pyplot(plt)

# NEW: Fasting Blood Sugar Distribution
st.subheader("Fasting Blood Sugar Distribution")
plt.figure(figsize=(8, 6))
sns.countplot(x='fbs', hue='target', data=df, palette='Set2')
plt.title("Fasting Blood Sugar > 120 mg/dL (1 = True, 0 = False)")
plt.xlabel("Fasting Blood Sugar")
plt.ylabel("Count")
st.pyplot(plt)

# NEW: ST Depression Induced by Exercise
st.subheader("ST Depression Induced by Exercise")
plt.figure(figsize=(8, 6))
sns.boxplot(x='target', y='oldpeak', data=df, palette='Set3')
plt.title("ST Depression Induced by Exercise")
plt.xlabel("Heart Disease (1 = Yes, 0 = No)")
plt.ylabel("ST Depression")
st.pyplot(plt)

# NEW: Number of Major Vessels Colored by Fluoroscopy
st.subheader("Number of Major Vessels Colored by Fluoroscopy")
plt.figure(figsize=(8, 6))
sns.countplot(x='ca', hue='target', data=df, palette='Set1')
plt.title("Number of Major Vessels Colored by Fluoroscopy")
plt.xlabel("Number of Major Vessels")
plt.ylabel("Count")
st.pyplot(plt)

# NEW: Thalassemia Type Distribution
st.subheader("Thalassemia Type Distribution")
plt.figure(figsize=(8, 6))
sns.countplot(x='thal', hue='target', data=df, palette='coolwarm')
plt.title("Thalassemia Type by Heart Disease")
plt.xlabel("Thalassemia Type (0-3)")
plt.ylabel("Count")
st.pyplot(plt)