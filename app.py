import streamlit as st
import requests
from groq import Groq

# 1. Setup Interface
st.title("🚢 Maritime Digital Twin AI")
st.sidebar.header("Configuration")
groq_key = st.sidebar.text_input("Enter Groq API Key", type="password")

# 2. Define Live Data Tools
def get_marine_weather(lat, lon):
    """Fetches live wave height and wind speed from Open-Meteo."""
    url = f"https://marine-api.open-meteo.com{lat}&longitude={lon}&current=wave_height,wind_speed_10m"
    res = requests.get(url).json()
    return res.get('current', "No data found")

# 3. Main Chat Logic
if groq_key:

    
    
    client = Groq(api_key=groq_key)
    
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

    if prompt := st.chat_input("Ex: What is the weather at Lat 1.3, Lon 103.8?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)

        # Simple logic: If user mentions 'weather', fetch it first
        if "weather" in prompt.lower():
            # In a world-class app, use Groq's Function Calling to extract Lat/Lon automatically
            weather_data = get_marine_weather(1.3, 103.8) # Example for Singapore
            context = f"The current live marine data is: {weather_data}. "
        else:
            context = ""

        # Get AI Response
        response = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            stream=False,
            messages=[{"role": "system", "content": "You are a Maritime Digital Twin expert. Use the provided live data to answer."}] + 
                     st.session_state.messages + 
                     [{"role": "system", "content": context}]
        )
        
        answer = response.choices[0].message.content
        st.session_state.messages.append({"role": "assistant", "content": answer})
        st.chat_message("assistant").write(answer)
