# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-08 06:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0009_auto_20181008_1438'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sessions',
            old_name='artivle',
            new_name='article',
        ),
    ]