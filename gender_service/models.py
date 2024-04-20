from django.db import models

# Create your models here.


class Gender(models.Model):
    gender = models.CharField(max_length=255)


class ManNames(models.Model):
    names_man = models.CharField(max_length=255)
    gender = models.ForeignKey(Gender, blank=True, on_delete=models.SET_NULL, default=None)


class WomenNames(models.Model):
    names_woman = models.CharField(max_length=255)
    gender = models.ForeignKey(Gender, blank=True, on_delete=models.SET_NULL, default=None)



# Женские имена таблица names_woman
# Мужские имена таблица names_man

