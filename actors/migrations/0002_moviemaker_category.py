# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-02-04 06:41
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('actors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviemaker',
            name='category',
            field=models.CharField(choices=[('professional', '\u041f\u0440\u043e\u0444\u0435\u0441\u0441\u0438\u043e\u043d\u0430\u043b'), ('normal', '\u041b\u044e\u0431\u0438\u0442\u0435\u043b\u044c'), ('newer', '\u041d\u043e\u0432\u0438\u0447\u043e\u043a')], default=datetime.datetime(2017, 2, 4, 6, 41, 13, 164173, tzinfo=utc), max_length=255),
            preserve_default=False,
        ),
    ]
