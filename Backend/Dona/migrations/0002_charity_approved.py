# Generated by Django 3.0.7 on 2020-06-18 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dona', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='charity',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
