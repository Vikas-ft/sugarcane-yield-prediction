import streamlit as st
import pickle
import pandas as pd

# Load trained model
model = pickle.load(open('yield_model.pkl', 'rb'))

# Website title
st.title("Sugarcane Yield Prediction")

st.write("Enter NDVI value to predict sugarcane yield (Tamil Nadu)")

# Input NDVI
ndvi = st.number_input("NDVI value (0 to 1)", min_value=0.0, max_value=1.0, step=0.01)

# Predict button
if st.button("Predict Yield"):
    input_data = pd.DataFrame([[ndvi]], columns=['NDVI'])
    prediction = model.predict(input_data)
    st.success(f"Predicted Yield: {prediction[0]:.2f} tonnes/hectare")
