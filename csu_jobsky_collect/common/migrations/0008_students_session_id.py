# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-03 15:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0007_auto_20181003_1912'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='session_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]