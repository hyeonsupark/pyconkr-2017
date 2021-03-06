# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-18 13:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0007_auto_20160416_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='payment_status',
            field=models.CharField(choices=[('ready', 'Ready'), ('paid', 'Paid'), ('deleted', 'Deleted')], default='ready', max_length=10),
        ),
        migrations.AlterField(
            model_name='registration',
            name='transaction_code',
            field=models.CharField(blank=True, max_length=36),
        ),
    ]
