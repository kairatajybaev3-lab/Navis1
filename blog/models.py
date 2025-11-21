from django.db import models


class Service(models.Model):
    img = models.ImageField("Иконка", upload_to="img/", null=True, blank=True)
    title = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Краткое описание ')
    details = models.TextField(verbose_name='Подробности')

    @property
    def path(self):

        return f"/media/{self.img}"

    @property
    def url(self):
        try:
            return self.img.url
        except:
            return None

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    def __str__(self):
        return f"{self.title}"
