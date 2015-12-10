# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('tag', models.CharField(max_length=25)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('purchase_date', models.DateTimeField(null=True)),
                ('make', models.CharField(null=True, max_length=25)),
                ('model', models.CharField(null=True, max_length=25)),
                ('issued_date', models.DateTimeField(null=True)),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(related_name='asset_owner', null=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AssetType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=25)),
                ('description', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='asset',
            name='type',
            field=models.ForeignKey(to='esat.AssetType', related_name='asset_type'),
        ),
    ]
