import streamlit as st
import joblib
import numpy as np

# Load the model from the current directory (no Windows path)
model = joblib.load('fraud_model.pkl')

st.title("💳 Credit Card Fraud Detection App")

st.markdown("Enter transaction details below:")

# Input fields for 31 features (V1 to V31)
input_features = []
for i in range(1, 32):
    value = st.number_input(f'V{i}', value=0.0, format="%.5f")
    input_features.append(value)

# Predict button
if st.button('Predict'):
    input_array = np.array([input_features])  # Shape: (1, 31)
    prediction = model.predict(input_array)

    if prediction[0] == 1:
        st.error("⚠️ Fraudulent Transaction Detected!")
    else:
        st.success("✅ Transaction is Genuine.")
