# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-18 10:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tree_menu', '0004_auto_20161117_1100'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='level',
            field=models.IntegerField(default=0, editable=False),
        ),
    ]
