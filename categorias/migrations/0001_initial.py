# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-25 11:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='categorias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('creado_el', models.DateTimeField(auto_now_add=True)),
                ('modificado_el', models.DateTimeField(auto_now=True)),
                ('visible', models.CharField(default='SI', max_length=2)),
            ],
        ),
    ]
