# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-11 09:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('terashare', '0004_file_stream'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='Course',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='terashare.Course'),
        ),
    ]
