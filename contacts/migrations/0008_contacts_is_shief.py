# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2019-12-06 08:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0007_auto_20190719_1443'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacts',
            name='is_shief',
            field=models.BooleanField(default=False),
        ),
    ]
