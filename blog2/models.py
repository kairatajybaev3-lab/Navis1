from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Contact(models.Model):
    email = models.EmailField("Электронная почта")
    phone = PhoneNumberField('Телефон',null=True, blank=True)
    created_at = models.DateTimeField("Создано", auto_now_add=True)

    def __str__(self):
        return f"{self.email} ({self.phone})"
