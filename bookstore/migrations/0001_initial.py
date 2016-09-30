# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-30 06:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isbn', models.CharField(max_length=6)),
                ('name', models.CharField(max_length=200)),
                ('price', models.IntegerField(default=0)),
                ('author', models.CharField(max_length=200)),
            ],
        ),
    ]