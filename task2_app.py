import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load('models/fraud_model.pkl')

st.title("Credit Card Fraud Detection")

st.markdown("Enter transaction details below:")

# Example input fields (adjust according to your features)
input_features = []
for i in range(1, 32):  # Assuming 31 features, e.g., V1, V2, ..., V31
    input_value = st.number_input(f'V{i}')
    input_features.append(input_value)

# Prediction button
if st.button('Predict'):
    # Convert the input features to a numpy array for prediction
    input_data = np.array([input_features])  # shape should be (1, 31)
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("⚠️ Fraudulent Transaction Detected!")
    else:
        st.success("✅ Transaction is Genuine.")
