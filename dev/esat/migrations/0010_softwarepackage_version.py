# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esat', '0009_auto_20160118_1810'),
    ]

    operations = [
        migrations.AddField(
            model_name='softwarepackage',
            name='version',
            field=models.CharField(null=True, blank=True, max_length=25),
        ),
    ]
