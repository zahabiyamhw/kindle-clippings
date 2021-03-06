# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-07-01 08:11
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clipping_manager', '0002_auto_20190624_1620'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailDelivery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interval', models.PositiveSmallIntegerField(choices=[(1, 'Daily'), (2, 'Bi-weekly'), (3, 'Weekly')], default=1, verbose_name='Interval')),
                ('last_delivery', models.DateTimeField(blank=True, null=True, verbose_name='Last successful delivery')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
    ]
