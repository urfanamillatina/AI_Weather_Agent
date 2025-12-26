import os, smtplib
from email.mime.text import MIMEText
from twilio.rest import Client

def send_email(body):
    sender = os.getenv("EMAIL_USER")
    password = os.getenv("EMAIL_PASS")
    to_addr = os.getenv("EMAIL_TO") or sender
    msg = MIMEText(body)
    msg["Subject"] = "🌦️ AI Weather Agent Update"
    msg["From"] = sender
    msg["To"] = to_addr
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as s:
            s.login(sender, password)
            s.send_message(msg)
        print("📧 Email sent to", to_addr)
    except Exception as e:
        print("Email error:", e)

def send_whatsapp(body):
    sid = os.getenv("TWILIO_SID")
    auth = os.getenv("TWILIO_AUTH")
    client = Client(sid, auth)
    from_no = os.getenv("TWILIO_FROM")
    to_no = os.getenv("TWILIO_TO")
    try:
        client.messages.create(from_=from_no, to=to_no, body=body)
        print("📱 WhatsApp message sent to", to_no)
    except Exception as e:
        print("Twilio error:", e)
