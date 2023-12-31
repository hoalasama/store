# Generated by Django 4.2.7 on 2023-11-26 07:37

from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stuff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=40)),
                ('profile_pic', django_resized.forms.ResizedImageField(crop=None, default='defaults/default_profile_pic.jpg', force_format=None, keep_meta=True, null=True, quality=100, scale=None, size=[400, 400], upload_to='authors')),
            ],
        ),
    ]
