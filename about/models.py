from django.db import models

class AboutInfo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    founder_name = models.CharField(max_length=100, verbose_name='Имя основателя')
    founder_image = models.ImageField("Фото Основателя", upload_to="img/", null=True, blank=True)
    founder_image1 = models.ImageField("Иконка1", upload_to="img/", null=True, blank=True)
    founder_image2 = models.ImageField("Иконка2", upload_to="img/", null=True, blank=True)
    founder_image3 = models.ImageField("Иконка3", upload_to="img/", null=True, blank=True)
    founder_image4 = models.ImageField("Иконка4", upload_to="img/", null=True, blank=True)
    founder_image5 = models.ImageField("Иконка5", upload_to="img/", null=True, blank=True)
    url_field = models.URLField('Подробности', null=True, blank=True)

    @property
    def path(self):

        return f"/media/{self.founder_image}"

    @property
    def url(self):
        try:
            return self.founder_image.url
        except:
            return None

    def __str__(self):
        return self.title


class Tool(models.Model):
    name = models.CharField(max_length=100)
    icon_img = models.ImageField("Иконка", upload_to="img/", null=True, blank=True)

    @property
    def path(self):

        return f"/media/{self.icon_img}"

    @property
    def url(self):
        try:
            return self.icon_img.url
        except:
            return None

    def __str__(self):
        return self.name