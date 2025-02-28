import streamlit as st
import joblib
import pandas as pd

# Load the saved model
#model = joblib.load('bestp_aqi_prediction_model.pkl')

import pickle

# Load the model
with open('bestp_aqi_prediction_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Title of the app
st.title('AQI Prediction App')

# Input fields for features
st.header('Enter Pollutant Levels and Temporal Features')
pm25 = st.number_input('PM2.5', value=50.0)
pm10 = st.number_input('PM10', value=100.0)
no2 = st.number_input('NO2', value=30.0)
co = st.number_input('CO', value=1.5)
so2 = st.number_input('SO2', value=10.0)
o3 = st.number_input('O3', value=40.0)
month = st.number_input('Month', value=3, min_value=1, max_value=12)
day_of_week = st.number_input('Day of Week', value=2, min_value=0, max_value=6)
quarter = st.number_input('Quarter', value=1, min_value=1, max_value=4)
aqi_lag1 = st.number_input('AQI Lag 1', value=120.0)

# Create a DataFrame from the input data
input_data = pd.DataFrame({
    'PM2.5': [pm25],
    'PM10': [pm10],
    'NO2': [no2],
    'CO': [co],
    'SO2': [so2],
    'O3': [o3],
    'Month': [month],
    'DayOfWeek': [day_of_week],
    'Quarter': [quarter],
    'AQI_lag1': [aqi_lag1]
})

# Predict AQI
if st.button('Predict AQI'):
    prediction = model.predict(input_data)
    st.success(f'Predicted AQI: {prediction[0]:.2f}')