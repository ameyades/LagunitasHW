# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-20 23:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0003_auto_20160520_2307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='score',
            field=models.DecimalField(decimal_places=1, default=0.0, max_digits=2),
            preserve_default=False,
        ),
    ]
