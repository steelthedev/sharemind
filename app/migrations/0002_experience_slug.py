# Generated by Django 3.2.4 on 2021-08-19 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]
