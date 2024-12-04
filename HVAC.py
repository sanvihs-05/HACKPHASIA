import streamlit as st
import pandas as pd
import numpy as np
import datetime
import random
import matplotlib.pyplot as plt


def get_simulated_data():
    return {
        "temperature": np.random.uniform(18, 30, 3).round(1),
        "air_quality": np.random.uniform(50, 100, 3).round(1),
        "energy_usage": np.random.uniform(100, 500, 3).round(1)
    }


def get_weather_forecast():
    return {
        "temperature": np.random.uniform(15, 25),
        "condition": random.choice(["Sunny", "Cloudy", "Rainy", "Stormy"])
    }


def get_energy_trends():
    dates = pd.date_range(datetime.datetime.now() - datetime.timedelta(days=30), periods=30)
    usage = np.random.uniform(100, 500, 30).round(1)
    return pd.DataFrame({"Date": dates, "Energy Usage": usage})

st.sidebar.title("Settings")
theme = st.sidebar.radio("Select Theme", ("Light Mode", "Dark Mode"))


if theme == "Dark Mode":
    st.markdown("""
        <style>
        .stApp {
            background-color: #2E2E2E;
            color: white;
        }
        </style>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
        <style>
        .stApp {
            background-color: white;
            color: black;
        }
        </style>
    """, unsafe_allow_html=True)


st.title("HVAC Control System")


st.header("Real-Time Dashboard")
data = get_simulated_data()
zones = ["Zone 1", "Zone 2", "Zone 3"]

for i, zone in enumerate(zones):
    st.subheader(zone)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Temperature (°C)", data["temperature"][i])
    with col2:
        st.metric("Air Quality (AQI)", data["air_quality"][i])
    with col3:
        st.metric("Energy Usage (kWh)", data["energy_usage"][i])


st.header("Manage HVAC Settings")
for zone in zones:
    st.subheader(zone)
    temperature = st.slider(f"Set Temperature for {zone} (°C)", 15, 30, 22)
    airflow = st.selectbox(f"Set Airflow for {zone}", ["Low", "Medium", "High"])
    mode = st.selectbox(f"Set Mode for {zone}", ["Eco", "Comfort", "Auto"])
    if st.button(f"Apply Settings for {zone}"):
        st.success(f"Settings applied for {zone}: Temperature {temperature}°C, Airflow {airflow}, Mode {mode}")


st.header("Weather Forecast")
weather = get_weather_forecast()
st.write(f"Forecasted Temperature: {weather['temperature']} °C")
st.write(f"Condition: {weather['condition']}")


st.header("Energy Usage Analytics")
energy_trends = get_energy_trends()

fig, ax = plt.subplots()
ax.plot(energy_trends['Date'], energy_trends['Energy Usage'], label='Energy Usage (kWh)')
ax.set_xlabel('Date')
ax.set_ylabel('Energy Usage (kWh)')
ax.set_title('Energy Usage Trends')
ax.legend()


st.pyplot(fig)


st.header("Notifications")
st.markdown("""
    <div style="background-color: #f9c2c2; padding: 10px; border-radius: 5px;">
        <strong>Alert:</strong> High energy usage detected in Zone 1!
    </div>
    <div style="background-color: #c2f9c2; padding: 10px; border-radius: 5px;">
        <strong>Tip:</strong> Consider switching to Eco mode to save energy.
    </div>
    <div style="background-color: #f9e0c2; padding: 10px; border-radius: 5px;">
        <strong>Maintenance Reminder:</strong> Check filters in Zone 2.
    </div>
""", unsafe_allow_html=True)


