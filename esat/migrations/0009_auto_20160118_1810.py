# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esat', '0008_auto_20160118_1805'),
    ]

    operations = [
        migrations.RenameField(
            model_name='softwarepackage',
            old_name='login_count',
            new_name='max_login_count',
        ),
    ]
