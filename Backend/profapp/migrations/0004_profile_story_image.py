# Generated by Django 3.0.7 on 2020-06-25 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profapp', '0003_auto_20200624_2250'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='story_image',
            field=models.ImageField(blank=True, upload_to='profiles/'),
        ),
    ]
