# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-20 17:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('terashare', '0011_delete_coursetimings'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseTimings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sunday', models.BooleanField()),
                ('Monday', models.BooleanField()),
                ('Tuesday', models.BooleanField()),
                ('Wednesday', models.BooleanField()),
                ('Thursday', models.BooleanField()),
                ('Friday', models.BooleanField()),
                ('Saturday', models.BooleanField()),
                ('From', models.TimeField()),
                ('To', models.TimeField()),
                ('course', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='terashare.Course')),
            ],
        ),
    ]
