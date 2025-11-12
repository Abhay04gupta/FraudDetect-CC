import streamlit as st
import numpy as np
import joblib

# Load model and scaler
model = joblib.load("credit_card_model.pkl")
scaler = joblib.load("scaler.pkl")

# Features
features = [f"V{i}" for i in range(1, 29)] + ["Amount"]
user_input = []

st.title("Credit Card Fraud Detection System")
st.header("Enter Transaction Details")

cols = st.columns(3)
for idx, feature in enumerate(features):
    with cols[idx % 3]:
        value = st.number_input(feature, value=0.0, format="%.5f")
        user_input.append(value)

# Convert to array
input_data = np.array([user_input])

# Scale only 'Amount' column if scaler was fit on one feature
input_data[:, -1:] = scaler.transform(input_data[:, -1:])

# Prediction
if st.button("Predict"):
    prediction = model.predict(input_data)
    if prediction[0] == 1:
        st.error("⚠️ The transaction is predicted as **Fraudulent**.")
    else:
        st.success("✅ The transaction is predicted as **Genuine**.")
