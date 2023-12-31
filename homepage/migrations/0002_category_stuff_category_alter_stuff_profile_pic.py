# Generated by Django 4.2.7 on 2023-11-26 07:52

from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='stuff',
            name='category',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AlterField(
            model_name='stuff',
            name='profile_pic',
            field=django_resized.forms.ResizedImageField(crop=None, default='defaults/default_profile_pic.jpg', force_format=None, keep_meta=True, null=True, quality=100, scale=None, size=[400, 400], upload_to='stuffs'),
        ),
    ]
