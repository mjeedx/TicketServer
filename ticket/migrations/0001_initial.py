# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-15 14:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tickets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('who', models.CharField(max_length=150)),
                ('subject', models.TextField()),
                ('where', models.CharField(max_length=200)),
                ('when', models.DateTimeField(auto_now=True)),
                ('date_end', models.DateTimeField(null=True)),
                ('finished', models.BooleanField(default=False)),
                ('deleted', models.BooleanField(default=False)),
                ('ip', models.CharField(blank=True, max_length=50)),
            ],
        ),
    ]
