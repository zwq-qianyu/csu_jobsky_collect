# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-02 03:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='name',
            field=models.CharField(default='ziyichen', max_length=16),
            preserve_default=False,
        ),
    ]