# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-03 14:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='category',
            name='views',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='page',
            name='like',
            field=models.IntegerField(default=0),
        ),
    ]
