# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-30 06:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_id',
            field=models.IntegerField(default=0),
        ),
    ]
