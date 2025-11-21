from django.db import models

class Vacancy(models.Model):
    CATEGORY_CHOICES = [
        ('frontend', 'Frontend'),
        ('backend', 'Backend'),
        ('fullstack', 'Fullstack'),
        ('python', 'Python'),
    ]
    LEVEL_CHOICES = [
        ('junior', 'Junior'),
        ('middle', 'Middle'),
        ('senior', 'Senior'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    level = models.CharField(max_length=10, choices=LEVEL_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return self.title