from django.db import models

# Create your models here.


class MenNames(models.Model):
    """
    Мужские имена таблица names_man
    """

    GENDER_CHOICES = (
        ('Мужской', 'М'),
    )
    names_man = models.CharField(max_length=255)
    bitrix_id = models.IntegerField(unique=True)
    gender = models.CharField(max_length=255, null=True, blank=True, choices=GENDER_CHOICES)

    def __str__(self):
        return self.names_man


class WomenNames(models.Model):
    """
    Женские имена таблица names_woman
    """

    GENDER_CHOICES = (
        ('Женский', 'Ж'),
    )
    names_woman = models.CharField(max_length=255)
    bitrix_id = models.IntegerField(unique=True)
    gender = models.CharField(max_length=255, null=True, blank=True, choices=GENDER_CHOICES)

    def __str__(self):
        return self.names_woman
