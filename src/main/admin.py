from django.contrib import admin
from . import models

# Register.
admin.site.register(models.Tag)
admin.site.register(models.Category)
admin.site.register(models.New)