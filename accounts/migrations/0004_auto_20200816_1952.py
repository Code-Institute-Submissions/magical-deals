# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-08-16 19:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200816_1939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercreate',
            name='add_Line_One',
            field=models.CharField(default='', max_length=254),
        ),
    ]
