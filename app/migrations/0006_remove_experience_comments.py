# Generated by Django 3.2.4 on 2021-08-22 11:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20210821_1947'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='experience',
            name='comments',
        ),
    ]
