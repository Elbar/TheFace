# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-02-07 10:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actors', '0004_project_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='body',
            field=models.CharField(choices=[('\u0445\u0443\u0434\u043e\u0435', '\u0445\u0443\u0434\u043e\u0435'), ('\u043e\u0431\u044b\u0447\u043d\u043e\u0435', '\u043e\u0431\u044b\u0447\u043d\u043e\u0435'), ('\u043f\u043b\u043e\u0442\u043d\u043e\u0435', '\u043f\u043b\u043e\u0442\u043d\u043e\u0435')], max_length=255, verbose_name='\u0422\u0435\u043b\u043e\u0441\u043b\u043e\u0436\u0435\u043d\u0438\u0435'),
        ),
    ]