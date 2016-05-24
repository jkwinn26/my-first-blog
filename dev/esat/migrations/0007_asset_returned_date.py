# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esat', '0006_auto_20160115_1643'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset',
            name='returned_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
