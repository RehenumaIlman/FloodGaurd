# import streamlit as st
# import folium
# from streamlit_folium import folium_static

# def flood_prone_areas_page():
#     st.title("Flood-Prone Areas")
#     st.write("Explore the regions in Bangladesh that are most vulnerable to flooding.")

#     # Create a map centered on Bangladesh
#     m = folium.Map(location=[23.6850, 90.3563], zoom_start=7)

#     # Add markers for flood-prone areas
#     flood_prone_areas = {
#         "Dhaka": (23.8103, 90.4125),
#         "Chittagong": (22.3569, 91.7832),
#         "Sylhet": (24.8949, 91.8687),
#         "Barisal": (22.7010, 90.3535),
#     }

#     for area, coords in flood_prone_areas.items():
#         folium.Marker(coords, popup=area).add_to(m)

#     # Display the map
#     folium_static(m)

import openmeteo_requests
import requests_cache
import pandas as pd
import folium
from retry_requests import retry

# Setup the Open-Meteo API client with cache and retry on error
cache_session = requests_cache.CachedSession('.cache', expire_after=3600)
retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
openmeteo = openmeteo_requests.Client(session=retry_session)

# List of coordinates for the desired locations in Bangladesh
locations = {
    "Chittagong": {"latitude": 22.3569, "longitude": 91.7832},
    "Sylhet": {"latitude": 24.8949, "longitude": 91.8687},
    "Barisal": {"latitude": 22.7010, "longitude": 90.3535},
    "Faridpur": {"latitude": 23.6075, "longitude": 89.8256},
    "Dhaka": {"latitude": 23.8103, "longitude": 90.4125},
    "Rangamati": {"latitude": 23.1680, "longitude": 92.1600},
    "Cox's Bazar": {"latitude": 21.4514, "longitude": 92.0112}
}

# API URL and parameters for flood risk prediction (adjusting based on available weather data)
url = "https://api.open-meteo.com/v1/forecast"
params = {
    "hourly": "precipitation,temperature_2m,wind_speed_10m",  # Precipitation, temperature, and wind speed
    "timezone": "Asia/Dhaka"
}

# Initialize folium map
flood_map = folium.Map(location=[23.8103, 90.4125], zoom_start=7)

# Fetch data for each location
for location, coords in locations.items():
    print(f"Fetching data for {location}...")

    # Update latitude and longitude for each location
    params["latitude"] = coords["latitude"]
    params["longitude"] = coords["longitude"]
    
    # Fetch data from Open-Meteo API
    responses = openmeteo.weather_api(url, params=params)

    # Check if response is valid
    if responses:
        response = responses[0]
        print(f"Coordinates: {response.Latitude()}°N {response.Longitude()}°E")
        print(f"Elevation: {response.Elevation()} m asl")
        print(f"Timezone: {response.Timezone()} {response.TimezoneAbbreviation()}")
        print(f"Timezone difference to GMT+0: {response.UtcOffsetSeconds()} s")

        # Process hourly data for temperature, precipitation, and wind speed
        hourly = response.Hourly()

        # Fetch hourly temperature, precipitation, and wind speed data
        hourly_temperature_2m = hourly.Variables(0).ValuesAsNumpy()
        hourly_precipitation = hourly.Variables(1).ValuesAsNumpy()
        hourly_wind_speed_10m = hourly.Variables(2).ValuesAsNumpy()

        # Create a DataFrame with the relevant data
        hourly_data = {
            "date": pd.date_range(
                start=pd.to_datetime(hourly.Time(), unit="s", utc=True),
                end=pd.to_datetime(hourly.TimeEnd(), unit="s", utc=True),
                freq=pd.Timedelta(seconds=hourly.Interval() * 60),
                inclusive="left"
            )
        }

        hourly_data["temperature_2m"] = hourly_temperature_2m
        hourly_data["precipitation"] = hourly_precipitation
        hourly_data["wind_speed_10m"] = hourly_wind_speed_10m

        # Create DataFrame for analysis
        hourly_dataframe = pd.DataFrame(data=hourly_data)

        # Display the dataframe with hourly weather data for this location
        print(hourly_dataframe)

        # Optional: Perform flood risk analysis based on the retrieved weather data
        # For example, high precipitation might indicate a risk of flooding
        hourly_dataframe["flood_risk"] = hourly_dataframe["precipitation"].apply(lambda x: "High" if x > 10 else "Low")

        # Show flood risk column (this is just an example, you can adjust the logic based on your actual flood model)
        print(hourly_dataframe[["date", "precipitation", "flood_risk"]])

        # Visualize flood risk on a map
        latest_flood_risk = hourly_dataframe["flood_risk"].iloc[-1]  # Use the latest data point
        color = 'red' if latest_flood_risk == 'High' else 'green'

        folium.Marker(
            location=[coords["latitude"], coords["longitude"]],
            popup=f"{location}: {latest_flood_risk}",
            icon=folium.Icon(color=color)
        ).add_to(flood_map)

    else:
        print(f"No data returned for {location}")

# Save or display the map
flood_map.save("flood_risk_map.html")

print("Flood risk map has been saved as 'flood_risk_map.html'.")

