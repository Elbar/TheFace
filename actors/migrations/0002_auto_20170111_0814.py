# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-01-11 08:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='status',
            field=models.CharField(choices=[('VIP', 'VIP'), ('BASIC', 'BASIC')], max_length=255, verbose_name='\u0421\u0442\u0430\u0442\u0443\u0441 \u0410\u043a\u0442\u0435\u0440\u0430'),
        ),
    ]
