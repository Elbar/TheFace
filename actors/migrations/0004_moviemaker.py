# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-01-23 09:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actors', '0003_auto_20170114_0521'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovieMaker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=255, verbose_name='')),
                ('lastname', models.CharField(max_length=255, verbose_name='')),
                ('surname', models.CharField(max_length=255, verbose_name='')),
                ('education', models.CharField(max_length=255, verbose_name='')),
                ('languages', models.CharField(max_length=255, verbose_name='')),
                ('ready_to_go', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=255)),
                ('experience', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': '',
            },
        ),
    ]