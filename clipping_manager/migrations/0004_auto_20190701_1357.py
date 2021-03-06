# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-07-01 13:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clipping_manager', '0003_emaildelivery'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='emaildelivery',
            options={'verbose_name': 'Email delivery', 'verbose_name_plural': 'Email deliveries'},
        ),
        migrations.AddField(
            model_name='emaildelivery',
            name='number_of_highlights',
            field=models.PositiveSmallIntegerField(default=5, verbose_name='Number of highlights to be sent per mail'),
        ),
    ]
