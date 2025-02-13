import streamlit as st
import requests

# Title of the app
st.title("🎈 My new app")

# Introductory text
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

# Function to get weather data
def get_weather(city):
    api_key = "Enter your API"  # API from weather API
    base_url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no"
    
    response = requests.get(base_url)
    data = response.json()
    
    if "error" in data:
        return f"Error: {data['error']['message']}"

    weather_info = {
        "City": data["location"]["name"],
        "Country": data["location"]["country"],
        "Temperature": f"{data['current']['temp_c']}°C",
        "Humidity": f"{data['current']['humidity']}%",
        "Pressure": f"{data['current']['pressure_mb']} hPa",
        "Wind Speed": f"{data['current']['wind_kph']} kph",
        "Condition": data["current"]["condition"]["text"]
    }
    
    return weather_info

# Streamlit UI
st.title("Weather App")
city_name = st.text_input("Enter city name:", "")

if city_name:
    weather = get_weather(city_name)
    
    if isinstance(weather, dict):
        for key, value in weather.items():
            st.write(f"**{key}:** {value}")
    else:
        st.error(weather)
