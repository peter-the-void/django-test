# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-17 11:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tree_menu', '0003_auto_20161117_0708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='from_menu',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='tree_menu.Menu'),
        ),
    ]
