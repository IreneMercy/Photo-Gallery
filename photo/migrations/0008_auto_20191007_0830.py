# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2019-10-07 05:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0007_auto_20191006_2224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='image_path',
            field=models.ImageField(upload_to='image/'),
        ),
    ]
