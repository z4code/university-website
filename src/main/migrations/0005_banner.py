# Generated by Django 5.1.1 on 2024-10-08 04:07

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_event_options_new_updated_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='uploads/banners')),
                ('URL', models.URLField(blank=True, help_text='Optional URL for the banner to link to.', null=True)),
                ('is_active', models.BooleanField(default=False)),
                ('start_date', models.DateTimeField(blank=True, help_text='Optional. Set when the banner should start showing.', null=True)),
                ('end_date', models.DateTimeField(blank=True, help_text='Optional. Set when the banner should stop showing.', null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Banner',
                'verbose_name_plural': 'Banners',
                'ordering': ['-created_at'],
            },
        ),
    ]
