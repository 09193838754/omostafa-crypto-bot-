import time
import requests

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
ELBANK_API_KEY = os.getenv("ELBANK_API_KEY")
ELBANK_API_SECRET = os.getenv("ELBANK_API_SECRET")

def send_message(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": CHAT_ID, "text": text})

while True:
    print("Bot is running…")
    time.sleep(10)
