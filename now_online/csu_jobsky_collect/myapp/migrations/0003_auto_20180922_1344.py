# Generated by Django 2.1.1 on 2018-09-22 05:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20180921_2347'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enterprises',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='students',
            name='end_time',
        ),
    ]
