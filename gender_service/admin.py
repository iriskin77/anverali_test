from django.contrib import admin
from .models import WomenNames, MenNames, Gender

# Register your models here.

admin.site.register(MenNames)
admin.site.register(WomenNames)
admin.site.register(Gender)
