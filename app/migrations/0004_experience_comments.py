# Generated by Django 3.2.4 on 2021-08-21 18:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20210821_1849'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='comments',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.comment'),
        ),
    ]
