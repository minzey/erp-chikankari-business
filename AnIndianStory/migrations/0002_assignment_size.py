# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-07-09 10:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AnIndianStory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='size',
            field=models.CharField(choices=[('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL')], default='--', max_length=10),
        ),
    ]
