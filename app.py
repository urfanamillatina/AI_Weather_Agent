from dotenv import load_dotenv
from weather_agent import get_weather
from ai_agent import ai_reason
from notify import send_email, send_whatsapp

load_dotenv()
print("🌦️ AI Weather Agent")
city = input("City: ")
question = input("Your question: ")

w = get_weather(city)
if not w:
    print("City not found.")
else:
    print("⛅", w)
    ans = ai_reason(w, question)
    print("🤖", ans)
    send_email(ans)
    send_whatsapp(ans)
    print("✅ Sent to Email and WhatsApp")
