# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-03 11:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0005_sessions_qr_imgname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enterprises',
            name='contacts',
            field=models.CharField(default='待填', max_length=32),
        ),
        migrations.AlterField(
            model_name='enterprises',
            name='phone',
            field=models.CharField(default='待填', max_length=16),
        ),
    ]
