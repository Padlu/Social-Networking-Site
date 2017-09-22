# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-20 16:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SocialNetworking', '0004_auto_20170920_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='user',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='signup',
            name='email_id',
            field=models.EmailField(default='', max_length=50),
        ),
    ]
