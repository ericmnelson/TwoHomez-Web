# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-23 20:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twohomez', '0006_home_neighborhood'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='pic_url',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
