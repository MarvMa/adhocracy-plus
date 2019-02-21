# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-03 11:18
from __future__ import unicode_literals

import adhocracy4.images.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('liqd_product_budgeting', '0015_proposal_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proposal',
            name='image',
            field=adhocracy4.images.fields.ConfiguredImageField('idea_image', blank=True, help_prefix='Visualize your idea.', upload_to='ideas/images'),
        ),
    ]
