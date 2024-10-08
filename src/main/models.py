from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

# Tag.
class Tag(models.Model):
	name = models.CharField(max_length=128)
	slug = models.SlugField(max_length=128, unique=True, blank=True, null=True)

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.name.lower())
		super().save(*args, **kwargs)

	def __str__(self) -> str:
		return self.name

# Category.
class Category(models.Model):

	class Meta:
		verbose_name = 'Category'
		verbose_name_plural = 'Categories'
	name = models.CharField(max_length=128)
	slug = models.SlugField(max_length=128, unique=True, blank=True, null=True)

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.name.lower())
		super().save(*args, **kwargs)

	def __str__(self) -> str:
		return self.name

# New.
class New(models.Model):
	title = models.CharField(max_length=255)
	author = models.ForeignKey(to=User, on_delete=models.CASCADE)
	attract = models.TextField(blank=True, null=True, max_length=510)
	image = models.ImageField(upload_to='uploads/news', blank=True, null=True)
	category = models.ForeignKey(to='Category', on_delete=models.CASCADE)
	tags = models.ManyToManyField(to='Tag', related_name='news')
	location = models.CharField(max_length=255, blank=True, null=True)
	location_URL = models.URLField(blank=True, null=True)
	content = models.TextField()
	views = models.PositiveIntegerField(default=0)
	is_published = models.BooleanField(default=False)
	publish_date = models.DateTimeField(blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self) -> str:
		return self.title

# Event.
class Event(models.Model):
	EVENT_TYPES = (
        ('CONF', 'Conference'),
        ('WEB', 'Webinar'),
        ('WORK', 'Workshop'),
        ('MEET', 'Meeting'),
    )

	title = models.CharField(max_length=255)
	description = models.TextField(blank=True, null=True)
	location = models.CharField(max_length=255, blank=True, null=True)
	location_URL = models.URLField(blank=True, null=True)
	event_type = models.CharField(max_length=5, choices=EVENT_TYPES, default='CONF')
	start_date = models.DateTimeField()
	end_date = models.DateTimeField()
	is_virtual = models.BooleanField(default=False)
	organizer = models.CharField(max_length=255, blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self) -> str:
		return self.title

	class Meta:
		ordering = ['start_date']
		verbose_name_plural = 'Events'

# Banner.
class Banner(models.Model):
	title = models.CharField(max_length=255)
	description = models.TextField(blank=True, null=True)
	image = models.ImageField(upload_to='uploads/banners', blank=True, null=True)
	URL = models.URLField(blank=True, null=True, help_text=_('Optional URL for the banner to link to.'))
	is_active = models.BooleanField(default=False)
	start_date = models.DateTimeField(blank=True, null=True, help_text=_('Optional. Set when the banner should start showing.'))
	end_date = models.DateTimeField(blank=True, null=True, help_text=_('Optional. Set when the banner should stop showing.'))
	created_at = models.DateTimeField(default=timezone.now)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self) -> str:
		return self.title

	class Meta:
		verbose_name = _('Banner')
		verbose_name_plural = _('Banners')
		ordering = ['-created_at']

# Virtual Reception.
class VirtualReception(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('responded', 'Responded'),
        ('resolved', 'Resolved'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True, null=True)
    department = models.CharField(max_length=100, blank=True, null=True)
    inquiry = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    response = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    responded_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"Inquiry from {self.name} - {self.status}"

    def mark_as_responded(self, response):
        self.status = 'responded'
        self.response = response
        self.responded_at = timezone.now()
        self.save()

    def mark_as_resolved(self):
        self.status = 'resolved'
        self.save()

    class Meta:
        verbose_name_plural = "Virtual Receptions"
        ordering = ['-created_at']

