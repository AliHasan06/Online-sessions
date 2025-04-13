
import streamlit as st

st.title("Karachi Weather App")
st.write("Created by Ali Hassan")

weather_data = {
    'Monday': {'temperature': 32, 'condition': 'Sunny'},
    'Tuesday': {'temperature': 34, 'condition': 'Humid'},
    'Wednesday': {'temperature': 30, 'condition': 'Cloudy'}
}

day = st.selectbox("Select a day", list(weather_data.keys()))
info = weather_data[day]

st.write(f"Temperature: {info['temperature']} °C")
st.write(f"Condition: {info['condition']}")
