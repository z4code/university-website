from django.contrib import admin
from . import models

# Register.
admin.site.register(models.Faculty)
admin.site.register(models.Specialization)
admin.site.register(models.Teacher)
admin.site.register(models.Dean)
admin.site.register(models.Curator)
admin.site.register(models.Manager)
admin.site.register(models.Course)
admin.site.register(models.Group)