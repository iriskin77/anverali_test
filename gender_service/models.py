from django.db import models

# Create your models here.


class Gender(models.Model):

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    gender = models.CharField(max_length=255, choices=GENDER_CHOICES)

    def __str__(self):
        return self.gender


class MenNames(models.Model):
    names_man = models.CharField(max_length=255)
    gender = models.ForeignKey(Gender, blank=True, on_delete=models.SET_NULL, null=True, default=None)

    def __str__(self):
        return self.names_man


class WomenNames(models.Model):
    names_woman = models.CharField(max_length=255)
    gender = models.ForeignKey(Gender, blank=True, on_delete=models.SET_NULL, null=True, default=None)

    def __str__(self):
        return self.names_woman



# Женские имена таблица names_woman
# Мужские имена таблица names_man

