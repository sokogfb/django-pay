# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-22 05:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pay', '0002_receipt_empty_paycard'),
    ]

    operations = [
        migrations.CreateModel(
            name='CVV',
            fields=[
                ('paycard', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='pay.PayCard')),
                ('encrypted', models.CharField(blank=True, editable=False, max_length=40, verbose_name='Encrypted CVV')),
            ],
        )
    ]
