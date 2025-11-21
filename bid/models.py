from phonenumber_field.modelfields import PhoneNumberField
from django.db import models


class ContactRequest(models.Model):
    name = models.CharField('Имя', max_length=40)
    phone = PhoneNumberField('Номер телефона', null=True, blank=True)
    message = models.TextField('Что вас интересует?', blank=True)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    processed = models.BooleanField('Обработано', default=False)

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
        ordering = ('-created_at',)

    def __str__(self):
        return f"{self.name or 'Без имени'}, - {self.phone}"
