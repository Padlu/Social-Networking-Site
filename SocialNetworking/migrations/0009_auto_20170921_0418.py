# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-21 04:18
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SocialNetworking', '0008_auto_20170920_2135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='birthdate',
            field=models.DateField(default=datetime.date(2017, 9, 21)),
        ),
    ]
