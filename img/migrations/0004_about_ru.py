# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-03-28 12:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('img', '0003_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='About_ru',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
            ],
        ),
    ]
