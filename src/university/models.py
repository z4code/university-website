from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
import datetime as dt

class Gender(models.TextChoices):
    MALE = 'M', _('Male')
    FEMALE = 'F', _('Female')

class Semester(models.TextChoices):
    FALL = 'F', _('Fall')
    SPRING = 'S', _('Spring')
    SUMMER = 'U', _('Summer')
    WINTER = 'W', _('Winter')

# Faculty.
class Faculty(models.Model):
    name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=10, blank=True, null=True)
    slug = models.SlugField(max_length=255, blank=True, null=True, unique=True)
    specializations = models.ManyToManyField('Specialization', related_name='faculties', blank=True)
    description = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name.lower())
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.short_name} - {self.name}' if self.short_name else self.name

    class Meta:
        verbose_name_plural = 'Faculties'
        ordering = ['name']

# Specialization.
class Specialization(models.Model):
    name = models.CharField(max_length=128)
    short_name = models.CharField(max_length=10, blank=True, null=True)
    slug = models.SlugField(max_length=128, blank=True, null=True, unique=True)
    code = models.CharField(max_length=30, unique=True)
    description = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name.lower())
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name} - {self.short_name}' if self.short_name else self.name

# Teacher.
class Teacher(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=1, choices=Gender.choices, default=Gender.MALE)
    image = models.ImageField(upload_to='uploads/teachers', blank=True, null=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)  # Updated to CharField
    specializations = models.ManyToManyField('Specialization', related_name='teachers')
    faculties = models.ManyToManyField('Faculty', related_name='teachers')
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name_plural = 'Teachers'
        ordering = ['first_name', 'last_name']

# Dean.
class Dean(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=1, choices=Gender.choices, default=Gender.MALE)
    image = models.ImageField(upload_to='uploads/deans', blank=True, null=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)  # Updated to CharField
    faculty = models.OneToOneField('Faculty', on_delete=models.SET_NULL, null=True)
    appointment_date = models.DateField()
    term_end_date = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name_plural = 'Deans'
        ordering = ['first_name', 'last_name']

# Curator.
class Curator(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=1, choices=Gender.choices, default=Gender.MALE)
    image = models.ImageField(upload_to='uploads/curators', blank=True, null=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    faculty = models.ForeignKey('Faculty', on_delete=models.SET_NULL, null=True)
    groups = models.ManyToManyField('Group', related_name='curators', blank=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name_plural = 'Curators'
        ordering = ['first_name', 'last_name']

# Manager.
class Manager(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=1, choices=Gender.choices, default=Gender.MALE)
    image = models.ImageField(upload_to='uploads/managers', blank=True, null=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    faculty = models.ForeignKey('Faculty', on_delete=models.SET_NULL, null=True)
    position = models.TextField(blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name_plural = 'Managers'
        ordering = ['first_name', 'last_name']

# Course.
class Course(models.Model):
    title = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128, blank=True, null=True, unique=True)
    year = models.IntegerField(default=dt.date.today().year)
    description = models.TextField(blank=True, null=True)
    credits = models.IntegerField(default=4)
    faculty = models.ForeignKey('Faculty', on_delete=models.SET_NULL, null=True)
    groups = models.ManyToManyField('Specialization', related_name='courses', blank=True)
    semester = models.CharField(max_length=1, choices=Semester.choices, default=Semester.FALL)
    students_count = models.IntegerField(default=12)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title.lower())
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Courses'
        ordering = ['title']

# Group.
class Group(models.Model):
    name = models.CharField(max_length=128)
    short_name = models.CharField(max_length=10, blank=True, null=True)
    slug = models.SlugField(max_length=128, blank=True, null=True, unique=True)
    year = models.IntegerField(default=dt.date.today().year)
    faculty = models.ForeignKey('Faculty', on_delete=models.SET_NULL, null=True)
    specialization = models.ForeignKey('Specialization', on_delete=models.SET_NULL, null=True)
    students_count = models.IntegerField(default=12)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name.lower())
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.short_name} - {self.name}' if self.short_name else self.name

    class Meta:
        verbose_name_plural = 'Groups'
        ordering = ['name', 'short_name']
