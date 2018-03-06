# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-19 12:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='Programme',
            field=models.CharField(choices=[('Btech', 'Btech'), ('Mtech', 'Mtech'), ('MA', 'MA'), ('Msc', 'Msc'), ('Phd', 'Phd'), ('Alumni', 'Alumni'), ('Staff', 'Staff')], max_length=99),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='Roll',
            field=models.CharField(max_length=8),
        ),
    ]
