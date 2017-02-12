# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-02-12 08:08
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('actors', '0006_projectstudio'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='projectstudio',
            options={'verbose_name': '\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u041f\u0440\u043e\u0435\u043a\u0442 Studio', 'verbose_name_plural': '\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u041f\u0440\u043e\u0435\u043a\u0442\u0430 Studio'},
        ),
        migrations.AddField(
            model_name='location',
            name='category',
            field=models.CharField(choices=[('Priroda', 'Priroda'), ('Interyer', 'Interyer')], default=datetime.datetime(2017, 2, 12, 8, 8, 58, 490563, tzinfo=utc), max_length=255),
            preserve_default=False,
        ),
    ]
