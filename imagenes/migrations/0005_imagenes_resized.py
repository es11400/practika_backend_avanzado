# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-19 09:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imagenes', '0004_auto_20161219_0938'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagenes',
            name='resized',
            field=models.BooleanField(default=False),
        ),
    ]
