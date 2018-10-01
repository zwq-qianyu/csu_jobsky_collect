# Generated by Django 2.1.1 on 2018-09-20 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Enterprises',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enterprise', models.CharField(max_length=200)),
                ('time', models.DateTimeField()),
                ('place', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'enterprise',
            },
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stu_name', models.CharField(max_length=60)),
                ('school', models.CharField(max_length=200)),
                ('major', models.CharField(max_length=200)),
                ('enterprise', models.CharField(max_length=200)),
                ('time', models.DateTimeField()),
                ('place', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'student',
            },
        ),
    ]
