# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2019-12-16 13:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tickets',
            name='when',
            field=models.DateTimeField(),
        ),
    ]
