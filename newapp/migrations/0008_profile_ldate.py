# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-16 11:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0007_auto_20180716_1714'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='ldate',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
