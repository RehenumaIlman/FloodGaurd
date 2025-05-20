# import streamlit as st

# def search_now_page():
#     st.title("Search Now")
#     st.write("Enter the required details to get flood predictions for your area.")

#     # Add input fields and prediction logic here
#     rainfall = st.number_input("Rainfall (mm)", min_value=0.0, max_value=500.0, value=50.0)
#     river_level = st.number_input("River Water Level (m)", min_value=0.0, max_value=20.0, value=5.0)
#     temperature = st.number_input("Temperature (°C)", min_value=0.0, max_value=50.0, value=25.0)

#     if st.button("Predict Flood Risk"):
#         input_data = np.array([[rainfall, river_level, temperature]])
#         prediction = predict_flood(input_data)
#         st.success(f"Flood Risk Prediction: {prediction[0]}")
import streamlit as st
import numpy as np
from geopy.geocoders import Nominatim  # Optional for reverse geocoding

# Optional reverse geocoding to get location name from coordinates
def get_location_name(lat, lng):
    geolocator = Nominatim(user_agent="flood_prediction")
    location = geolocator.reverse((lat, lng), language="en")
    return location.address if location else "Unknown Location"

def validate_coordinates(lat, lng):
    try:
        lat = float(lat)
        lng = float(lng)
        if -90 <= lat <= 90 and -180 <= lng <= 180:
            return True
        else:
            return False
    except ValueError:
        return False

def search_now_page():
    st.title("Search Now")
    st.write("Enter the required details to get flood predictions for your area.")

    # Add input fields for rainfall, river level, and temperature
    rainfall = st.number_input("Rainfall (mm)", min_value=0.0, max_value=500.0, value=50.0)
    river_level = st.number_input("River Water Level (m)", min_value=0.0, max_value=20.0, value=5.0)
    temperature = st.number_input("Temperature (°C)", min_value=0.0, max_value=50.0, value=25.0)

    # Add input fields for latitude and longitude
    lat = st.text_input("Enter Latitude:")
    lng = st.text_input("Enter Longitude:")

    # Validate coordinates
    if lat and lng and validate_coordinates(lat, lng):
        location_name = get_location_name(lat, lng)  # Optional: To get the location name
        st.write(f"Location: {location_name}")
    else:
        st.error("Invalid coordinates. Please enter valid latitude and longitude.")

    if st.button("Predict Flood Risk"):
        if lat and lng and validate_coordinates(lat, lng):
            input_data = np.array([[rainfall, river_level, temperature, float(lat), float(lng)]])
            
            # Assuming you have a prediction model, e.g., predict_flood(input_data)
            prediction = predict_flood(input_data)
            
            # Display the flood risk prediction
            st.success(f"Flood Risk Prediction: {prediction[0]}")
        else:
            st.error("Please enter valid coordinates to get a prediction.")
