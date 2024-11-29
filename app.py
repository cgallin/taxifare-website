import streamlit as st
import requests
'''
#TaxiFareModel front
'''
pickup_datetime = st.text_input('Pickup Date and time')
pickup_longitude=st.number_input('Pickup Longitude')
pickup_latitude=st.number_input('Pickup Latitude')
dropoff_longitude=st.number_input('Dropoff Longitude')
dropoff_latitude=st.number_input('Dropoff Latitude')
passenger_count = st.slider('Select a line count', 1, 6,1)




url = 'https://taxifare.lewagon.ai/predict'
dict = {
    "pickup_datetime": pickup_datetime,
    "pickup_longitude": pickup_longitude,
    "pickup_latitude": pickup_latitude,
    "dropoff_longitude": dropoff_longitude,
    "dropoff_latitude": dropoff_latitude,
    "passenger_count": passenger_count
}

if st.button('Predict'):
    prediction = requests.get(url, params=dict).json()
    st.write("Predicted Cost", prediction)
