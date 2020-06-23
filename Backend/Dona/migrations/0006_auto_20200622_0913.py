# Generated by Django 3.0.7 on 2020-06-22 09:13

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('Dona', '0005_donor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donor',
            name='phone_number',
        ),
        migrations.AddField(
            model_name='donor',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(default=None, max_length=128, region=None, unique=True),
        ),
    ]
