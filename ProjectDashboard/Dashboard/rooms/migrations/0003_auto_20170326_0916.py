# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-26 03:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0002_auto_20170326_0915'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accomodationform',
            name='Datefrom',
        ),
        migrations.RemoveField(
            model_name='accomodationform',
            name='Dateto',
        ),
    ]