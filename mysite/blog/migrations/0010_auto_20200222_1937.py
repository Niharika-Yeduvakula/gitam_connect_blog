# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-02-22 14:07
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20200222_1928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 22, 14, 7, 56, 723945, tzinfo=utc)),
        ),
    ]
