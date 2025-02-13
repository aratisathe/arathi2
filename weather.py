import streamlit as st
import requests
import os

# Function to get weather data
def get_weather(city, api_key):
    try:
        url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no'
        response = requests.get(url)
        response.raise_for_status()  # Check for errors
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": {"message": str(e)}}

# Streamlit app
def main():
    st.title("🌤 Real-Time Weather App")

    api_key = os.getenv("WEATHER_API_KEY", "your_default_api_key")  # Get API key from env

    city = st.text_input("Enter city name")

    if st.button("Get Weather"):
        if city:
            data = get_weather(city, api_key)
            if "error" in data:
                st.error(f"Error: {data['error']['message']}")
            else:
                col1, col2 = st.columns([2, 1])

                with col1:
                    st.subheader(f"Weather in {data['location']['name']}, {data['location']['country']}")
                    st.write(f"**Condition:** {data['current']['condition']['text']}")

                with col2:
                    st.image(f"http:{data['current']['condition']['icon']}", width=80)

                st.metric("🌡 Temperature", f"{data['current']['temp_c']}°C")
                st.metric("🤒 Feels Like", f"{data['current']['feelslike_c']}°C")
                st.metric("💧 Humidity", f"{data['current']['humidity']}%")
                st.metric("🌬 Wind Speed", f"{data['current']['wind_kph']} kph")
                st.metric("🔵 Pressure", f"{data['current']['pressure_mb']} hPa")
                st.metric("☀ UV Index", f"{data['current']['uv']}")
                st.metric("👀 Visibility", f"{data['current']['vis_km']} km")
        else:
            st.warning("Please enter a city name")

if __name__ == "__main__":
    main()
