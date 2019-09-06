# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-09-06 10:35
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clipping_manager', '0005_emaildelivery_active'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='clipping',
            options={'ordering': ('user', 'book', 'author_name'), 'verbose_name': 'Clipping', 'verbose_name_plural': 'Clippings'},
        ),
        migrations.AddField(
            model_name='book',
            name='author_name',
            field=models.CharField(blank=True, max_length=500, verbose_name='Author'),
        ),
        migrations.AddField(
            model_name='clipping',
            name='author_name',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Author'),
        ),
        migrations.AddField(
            model_name='clipping',
            name='url',
            field=models.URLField(blank=True, null=True, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='clipping',
            name='book',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clipping_manager.Book', verbose_name='Book'),
        ),
        migrations.AlterUniqueTogether(
            name='clipping',
            unique_together=set([('user', 'content')]),
        ),
    ]
