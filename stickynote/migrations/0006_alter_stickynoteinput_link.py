# Generated by Django 4.0.6 on 2022-08-24 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stickynote', '0005_stickynoteinput_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stickynoteinput',
            name='link',
            field=models.TextField(max_length=5000),
        ),
    ]