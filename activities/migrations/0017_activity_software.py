# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-06 16:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0016_concept_software'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='software',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='activities.Software'),
            preserve_default=False,
        ),
    ]
