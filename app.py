import streamlit as st
'''
#TaxiFareModel front
'''
pickup_longitude=st.number_input('pickup_longitude')
pickup_latitude=st.number_input('pickup_latitude')
dropoff_longitude=st.number_input('dropoff_longitude')
dropoff_latitude=st.number_input('dropoff_latitude')
passenger_count=st.integer_input('passenger_count',min_value=1, max_value=8)
st.button('Predict')

url = 'https://taxifare.lewagon.ai/predict'

dict = {
    "pickup_longitude": pickup_longitude,
    "pickup_latitude": pickup_latitude,
    "dropoff_longitude": dropoff_longitude,
    "dropoff_latitude": dropoff_latitude,
    "passenger_count": passenger_count
}

prediction = requests.get(url, params=dict).json()
st.write("Predicted Cost", prediction['prediction'])
