# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-09-19 07:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adoptions', '0002_auto_20190919_1222'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Pets',
            new_name='Pet',
        ),
    ]
