# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-23 22:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twohomez', '0009_auto_20170423_2240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='address1',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
