from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Space)
admin.site.register(models.Topic)
admin.site.register(models.Message)