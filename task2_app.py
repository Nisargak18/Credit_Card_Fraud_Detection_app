import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load('fraud_model.pkl')

st.title("Credit Card Fraud Detection")

st.markdown("Enter transaction details below:")

# Example input fields (adjust according to your features)
# You may need to scale inputs if your model expects scaled data
v1 = st.number_input('V1')
v2 = st.number_input('V2')
v3 = st.number_input('V3')
v4 = st.number_input('V4')
v5 = st.number_input('V5')
norm_amount = st.number_input('Normalized Amount')
norm_time = st.number_input('Normalized Time')

# Predict button
if st.button('Predict'):
    input_data = np.array([[v1, v2, v3, v4, v5, norm_amount, norm_time]])  # adjust length to your features
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("⚠️ Fraudulent Transaction Detected!")
    else:
        st.success("✅ Transaction is Genuine.")
