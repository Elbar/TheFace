# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-01-25 11:01
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('actors', '0006_auto_20170125_1051'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviemaker',
            name='job_type',
            field=models.CharField(default=datetime.datetime(2017, 1, 25, 11, 1, 42, 879927, tzinfo=utc), max_length=255, verbose_name='\u0421\u043f\u0435\u0446\u0438\u0430\u043b\u0438\u0437\u0430\u0446\u0438\u044f'),
            preserve_default=False,
        ),
    ]
