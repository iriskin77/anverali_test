from django.contrib import admin
from .models import WomenNames, MenNames

# Register your models here.

admin.site.register(MenNames)
admin.site.register(WomenNames)
