# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esat', '0005_auto_20160115_1640'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='termination_cause',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='termination_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
