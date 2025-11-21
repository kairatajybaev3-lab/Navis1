import os
import requests
from bid.models import ContactRequest


TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def send_telegram_notification(contact: "ContactRequest"):
    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
        return

    text = (
        f"Новая заявка:\n"
        f"Имя: {contact.name or '-'}\n"
        f"Телефон: {contact.phone}\n"
        f"Сообщение: {contact.message or '-'}\n"
        f"Время: {contact.created_at.strftime('%Y-%m-%d %H:%M:%S')}"
    )
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": text}
    r = requests.post(url, json=payload, timeout=5)
    r.raise_for_status()