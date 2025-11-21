import requests
from django.db.models.signals import post_save
from django.dispatch import receiver

from blog2.models import Contact
from config import settings

TELEGRAM_BOT_TOKEN = settings.env("BOT_TOKEN")
CHAT_ID = settings.env("CHAT_ID")


@receiver(post_save, sender=Contact)
def send_to_telegram(sender, instance, created, **kwargs):
    if created:
        message = (
            f"Новая заявка через админку!\n"
            f"Email: {instance.email}\n"
            f"Телефон: {instance.phone}"
        )

        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
        data = {"chat_id": CHAT_ID, "text": message, "parse_mode": "Markdown"}
        try:
            requests.post(url, data=data, timeout=5)
        except Exception as e:
            print(f"Ошибка Telegram: {e}")