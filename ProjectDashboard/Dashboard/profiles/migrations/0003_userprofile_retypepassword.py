# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-19 12:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20170319_1805'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='ReTypePassword',
            field=models.CharField(default=1, max_length=150),
        ),
    ]