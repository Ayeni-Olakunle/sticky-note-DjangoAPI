# Generated by Django 4.1 on 2022-08-23 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stickynote', '0003_stickynoteinput_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='stickynoteinput',
            name='time',
            field=models.TimeField(auto_now=True),
        ),
    ]