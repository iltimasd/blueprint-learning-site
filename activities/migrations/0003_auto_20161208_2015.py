# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-08 20:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0002_auto_20161208_2014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
