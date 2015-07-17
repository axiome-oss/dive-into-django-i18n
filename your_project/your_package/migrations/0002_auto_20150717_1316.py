# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('your_package', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='description_en',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='description_fr',
            field=models.TextField(null=True, blank=True),
        ),
    ]
