from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

# Tag.
class Tag(models.Model):
	name = models.CharField(max_length=128)
	slug = models.SlugField(max_length=128, unique=True, blank=True, null=True)

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.name.lower())
		super().save(*args, **kwargs)

	def __str__(self):
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

	def __str__(self):
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

	def __str__(self):
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

	def __str__(self):
		return self.title

	class Meta:
		ordering = ['start_date']
		verbose_name_plural = 'Events'