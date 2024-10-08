from django.contrib import admin
from . import models
from django.contrib.auth.models import User, Group

# Register.
admin.site.register(models.Tag)
admin.site.register(models.Category)
admin.site.register(models.New)
admin.site.register(models.Event)
admin.site.register(models.Banner)
admin.site.register(models.VirtualReception)

# Unregister.
admin.site.unregister(Group)