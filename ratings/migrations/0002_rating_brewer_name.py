# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-19 19:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='brewer_name',
            field=models.TextField(default='Lagunitas'),
            preserve_default=False,
        ),
    ]