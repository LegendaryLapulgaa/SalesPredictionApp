import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load('sales_model.pkl')

st.title("Sales Prediction App")
st.write("Enter advertising spend to predict sales")

tv = st.number_input("TV Advertising Budget", min_value=0.0)
radio = st.number_input("Radio Advertising Budget", min_value=0.0)
newspaper = st.number_input("Newspaper Advertising Budget", min_value=0.0)

if st.button("Predict"):
    features = pd.DataFrame([[tv, radio, newspaper]], columns=['TV', 'Radio', 'Newspaper'])
    prediction = model.predict(features)
    st.success(f"Predicted Sales: {prediction[0]:.2f}")
