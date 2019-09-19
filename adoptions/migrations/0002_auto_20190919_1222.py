# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-09-19 06:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adoptions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pets',
            name='description',
            field=models.TextField(default='NO Decription Provided'),
        ),
        migrations.AlterField(
            model_name='pets',
            name='sex',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1),
        ),
    ]
