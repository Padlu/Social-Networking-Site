# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-21 06:33
from __future__ import unicode_literals

import SocialNetworking.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SocialNetworking', '0013_auto_20170921_0626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='display',
            field=models.ImageField(blank=True, default='/user_profile/images.png', upload_to=SocialNetworking.models.image_upload_user),
        ),
    ]
