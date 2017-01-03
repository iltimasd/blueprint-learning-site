# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-20 17:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0004_auto_20161208_2023'),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='activity',
            name='grade_name',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='activity',
            name='subject_name',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='activity',
            name='grade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activities.Grade'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activities.Subject'),
        ),
        migrations.AddField(
            model_name='activity',
            name='devices',
            field=models.ManyToManyField(to='activities.Device'),
        ),
    ]
