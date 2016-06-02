# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-20 22:47
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
            field=models.CharField(default='Lagunitas', max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='rating',
            name='beer_name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='rating',
            name='notes',
            field=models.CharField(max_length=20),
        ),
    ]
