# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-11-28 14:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('duet_account', '0005_auto_20161009_1306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allowancededuction',
            name='code',
            field=models.CharField(default='kjj', max_length=10, unique=True, verbose_name='Code'),
            preserve_default=False,
        ),
    ]
