# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esat', '0002_auto_20151202_1731'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='asset',
            name='decommission_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='asset',
            name='make',
            field=models.CharField(blank=True, default='', max_length=25),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='asset',
            name='model',
            field=models.CharField(blank=True, default='', max_length=25),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='assettype',
            name='description',
            field=models.CharField(max_length=100),
        ),
    ]
