# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-02-07 10:05
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('actors', '0003_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='title',
            field=models.CharField(default=datetime.datetime(2017, 2, 7, 10, 5, 39, 177549, tzinfo=utc), max_length=255, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043f\u0440\u043e\u0435\u043a\u0442\u0430'),
            preserve_default=False,
        ),
    ]
