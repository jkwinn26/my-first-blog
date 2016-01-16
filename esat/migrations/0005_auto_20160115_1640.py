# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esat', '0004_department_employee'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='work_location',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='employee',
            name='phone_extn',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]
