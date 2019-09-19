# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-09-19 06:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('submitter', models.CharField(max_length=20)),
                ('species', models.CharField(max_length=20)),
                ('breed', models.CharField(max_length=20)),
                ('sex', models.CharField(choices=[('m', 'Male'), ('f', 'Female')], max_length=1)),
                ('age', models.IntegerField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Vaccine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='pets',
            name='vaccinations',
            field=models.ManyToManyField(to='adoptions.Vaccine'),
        ),
    ]
