import time
import os
import requests

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
ELBANK_API_KEY = os.getenv("ELBANK_API_KEY")
ELBANK_API_SECRET = os.getenv("ELBANK_API_SECRET")

def send_telegram(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {"chat_id": "8506536121", "text": message}
    requests.post(url, data=data)

def get_price():
    url = "https://api.albank.exchange/v1/market/ticker?symbol=BTCUSDT"
    r = requests.get(url).json()
    return float(r["price"])

send_telegram("ربات معامله‌گر شروع شد")

while True:
    try:
        price = get_price()
        send_telegram(f"قیمت فعلی BTC: {price}")
    except Exception as e:
        send_telegram(f"Error: {e}")

    time.sleep(60)
