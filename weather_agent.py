import os, requests

def get_weather(city: str):
    print("City => ",city)
    key = os.getenv("WEATHER_API_KEY")
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&units=metric"
    r = requests.get(url).json()
    if r.get("cod") != 200:
        return None
    desc = r["weather"][0]["description"]
    temp = r["main"]["temp"]
    hum = r["main"]["humidity"]
    return f"The weather in {city.title()} is {desc}, temperature {temp}°C, humidity {hum}%."
