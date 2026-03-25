import streamlit as st
import pandas as pd
import pickle

# Load trained district-level model
model = pickle.load(open('yield_model.pkl', 'rb'))

# Load district NDVI dataset
data = pd.read_csv('TamilNadu_District_NDVI_Yield.csv')

st.title("Sugarcane Yield Prediction using Satellite Data")
st.write("District-wise sugarcane yield prediction for Tamil Nadu")

# District selection dropdown
district = st.selectbox(
    "Select District",
    sorted(data['District'].unique())
)

# Fetch NDVI of selected district
selected_row = data[data['District'] == district].iloc[0]
avg_ndvi = selected_row['Avg_NDVI']

# Predict yield
if st.button("Predict Yield"):
    input_data = pd.DataFrame([[avg_ndvi]], columns=['Avg_NDVI'])
    prediction = model.predict(input_data)

    st.success(
        f"District: {district}\n"
        f"Average NDVI: {avg_ndvi:.3f}\n"
        f"Predicted Yield: {prediction[0]:.2f} tonnes/hectare"
    )
