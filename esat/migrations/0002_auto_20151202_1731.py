# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('esat', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asset',
            name='owner',
        ),
        migrations.AddField(
            model_name='asset',
            name='assigned_user',
            field=models.ForeignKey(related_name='asset_owner', blank=True, null=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='asset',
            name='issued_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='asset',
            name='purchase_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
