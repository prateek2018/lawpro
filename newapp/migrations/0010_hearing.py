# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-16 12:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0009_remove_profile_ldate'),
    ]

    operations = [
        migrations.CreateModel(
            name='hearing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lst', models.CharField(max_length=30)),
                ('nxt', models.CharField(max_length=30)),
            ],
        ),
    ]