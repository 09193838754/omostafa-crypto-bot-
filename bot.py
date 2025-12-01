import time
import os
import requests

# ====== Load Secrets ======
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
ELBANK_API_KEY = os.getenv("ELBANK_API_KEY")
ELBANK_API_SECRET = os.getenv("ELBANK_API_SECRET")

CHAT_ID = "8506536121"   # چت آیدی تو

# ====== Telegram Function ======
def send_telegram(message):
    if not TELEGRAM_TOKEN:
        print("❌ Telegram token is missing!")
        return

    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message}

    try:
        requests.post(url, data=data)
    except:
        print("❌ Error sending Telegram message")

# ====== Get Price from ElBank ======
def get_price():
    url = "https://api.albank.exchange/v1/market/ticker?symbol=BTCUSDT"
    try:
        r = requests.get(url, timeout=10).json()

        # API مقدار را در داخل result قرار می‌دهد
        if "result" in r and "price" in r["result"]:
            return float(r["result"]["price"])
        elif "price" in r:
            return float(r["price"])
        else:
            raise Exception("Invalid API response")

    except Exception as e:
        send_telegram(f"❌ API ERROR: {e}")
        return None

# ====== Start Bot ======
send_telegram("✅ ربات 24/7 ال بانک روشن شد")

# ====== Main Loop ======
while True:
    price = get_price()

    if price is not None:
        send_telegram(f"📊 قیمت لحظه‌ای BTC : {price}")

    time.sleep(60)
