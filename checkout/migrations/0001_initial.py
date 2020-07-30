# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-07-30 11:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0003_auto_20200722_0023'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_Number', models.CharField(max_length=20)),
                ('address_Line_One', models.CharField(max_length=40)),
                ('address_Line_Two', models.CharField(max_length=40)),
                ('address_Line_Three', models.CharField(max_length=40)),
                ('town_or_City', models.CharField(max_length=40)),
                ('county', models.CharField(max_length=40)),
                ('postcode', models.CharField(blank=True, max_length=40)),
                ('country', models.CharField(max_length=40)),
                ('date', models.DateField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderLineItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='checkout.Order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product')),
            ],
        ),
    ]
