# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-13 00:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ghtelectroniccenter', '0005_auto_20170106_1030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='harga',
            name='harga',
            field=models.IntegerField(default=1),
        ),
    ]
