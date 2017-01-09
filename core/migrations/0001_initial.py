# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-09 13:36
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True, verbose_name='nome')),
                ('created_date', models.DateTimeField(default=datetime.datetime(2017, 1, 9, 13, 36, 12, 333775, tzinfo=utc), verbose_name='Data de Cadastro')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('confirm', models.BooleanField(default=False, verbose_name='Cadastro confirmado')),
                ('confirm_date', models.DateTimeField(blank=True, null=True, verbose_name='Data de confirmação')),
                ('hash', models.CharField(blank=True, max_length=200, null=True, verbose_name='hash')),
                ('date_hash', models.DateTimeField(blank=True, null=True, verbose_name='data hash')),
            ],
        ),
    ]
