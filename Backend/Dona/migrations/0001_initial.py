# Generated by Django 3.0.7 on 2020-06-18 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Donations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.CharField(max_length=100)),
                ('currency', models.CharField(max_length=10)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
