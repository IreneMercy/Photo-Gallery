# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2019-10-06 13:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='image_path',
            field=models.ImageField(upload_to='images/'),
        ),
    ]