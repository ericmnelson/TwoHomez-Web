# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-23 19:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twohomez', '0002_auto_20170423_1904'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='zip_code',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
