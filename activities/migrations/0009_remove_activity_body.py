# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-24 21:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0008_auto_20161222_1937'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='body',
        ),
    ]
