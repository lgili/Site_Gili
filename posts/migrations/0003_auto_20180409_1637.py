# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-04-09 16:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_metatag'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='keywords',
            field=models.CharField(default='keywords', max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='metatag',
            field=models.CharField(default='metatag', max_length=200),
        ),
    ]
