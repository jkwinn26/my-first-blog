# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('esat', '0007_asset_returned_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='SoftwarePackage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=2, choices=[('PC', 'PC Client Install'), ('LW', 'Internal Website/System'), ('RW', 'External Website/System')], default='PC')),
                ('multiple_logins', models.BooleanField(default=False)),
                ('login_count', models.PositiveSmallIntegerField(default=1)),
                ('ip_address', models.GenericIPAddressField(protocol='IPv4')),
                ('port_number', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('url', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SoftwareVendor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('support_email', models.EmailField(max_length=254)),
                ('support_phone', models.CharField(max_length=17, blank=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
            ],
        ),
        migrations.AddField(
            model_name='softwarepackage',
            name='vendor',
            field=models.ForeignKey(to='esat.SoftwareVendor'),
        ),
    ]
