# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-05-18 20:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0022_resource'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResourceTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='resource',
            name='tags',
            field=models.ManyToManyField(to='activities.ResourceTag'),
        ),
    ]
