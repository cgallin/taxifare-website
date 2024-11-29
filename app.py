import streamlit as st
import requests
'''
#TaxiFareModel front
'''
pickup_longitude=st.number_input('pickup_longitude')
pickup_latitude=st.number_input('pickup_latitude')
dropoff_longitude=st.number_input('dropoff_longitude')
dropoff_latitude=st.number_input('dropoff_latitude')
passenger_count = st.slider('Select a line count', 1, 6,1)




url = 'https://taxifare.lewagon.ai/predict'
dict = {
    "pickup_longitude": pickup_longitude,
    "pickup_latitude": pickup_latitude,
    "dropoff_longitude": dropoff_longitude,
    "dropoff_latitude": dropoff_latitude,
    "passenger_count": passenger_count
}

if st.button('Predict'):
    prediction = requests.get(url, params=dict).json()
    st.write("Predicted Cost", prediction['prediction'])
