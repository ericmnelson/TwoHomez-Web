# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-23 22:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twohomez', '0007_auto_20170423_2002'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='sale_type',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
