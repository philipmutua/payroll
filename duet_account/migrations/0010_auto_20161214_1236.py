# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-12-14 06:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('duet_account', '0009_auto_20161214_1208'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gpfadvance',
            old_name='is_confirmed',
            new_name='is_freezed',
        ),
        migrations.RenameField(
            model_name='homeloan',
            old_name='is_confirmed',
            new_name='is_freezed',
        ),
    ]