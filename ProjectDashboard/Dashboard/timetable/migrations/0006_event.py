# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-22 12:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0005_auto_20170320_2306'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=50)),
                ('event_day', models.CharField(choices=[('Sun', 'Sun'), ('Mon', 'Mon'), ('Tue', 'Tue'), ('Wed', 'Wed'), ('Thu', 'Thu'), ('Fri', 'Fri'), ('Sat', 'Sat')], max_length=50)),
                ('event_time_from', models.TimeField()),
                ('event_time_to', models.TimeField()),
            ],
        ),
    ]