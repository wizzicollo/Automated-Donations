# Generated by Django 3.0.7 on 2020-06-29 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dona', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StoryMini',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
            ],
        ),
        migrations.RemoveField(
            model_name='story',
            name='story_image',
        ),
    ]
