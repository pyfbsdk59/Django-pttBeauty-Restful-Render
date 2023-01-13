from django.contrib import admin

# Register your models here.
from images import models
from images.models import Images
admin.site.register(models.Images)