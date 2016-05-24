# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esat', '0003_auto_20151203_0833'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('number', models.PositiveSmallIntegerField()),
                ('name', models.CharField(max_length=50)),
                ('supervisor', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employee_id', models.CharField(serialize=False, primary_key=True, max_length=5)),
                ('last_name', models.CharField(max_length=75)),
                ('first_name', models.CharField(max_length=75)),
                ('middle_name', models.CharField(max_length=50)),
                ('job_title', models.CharField(max_length=50)),
                ('emp_type', models.CharField(max_length=2, choices=[('FT', 'Full-time'), ('PT', 'Part-time'), ('CF', 'Contractor full-time'), ('CP', 'Contractor part-time'), ('SF', 'Student full-time'), ('SP', 'Student part-time')], default='FT')),
                ('new_phone', models.BooleanField(default=False)),
                ('outside_line', models.BooleanField(default=False)),
                ('phone_extn', models.PositiveSmallIntegerField()),
                ('start_date', models.DateField()),
                ('department', models.ForeignKey(to='esat.Department')),
            ],
        ),
    ]
