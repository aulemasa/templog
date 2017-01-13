# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('room', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='TempMeasurmentsValues',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('temp_value', models.DecimalField(verbose_name='Temperatura', max_digits=5, decimal_places=2)),
                ('tepm_measurment_data', models.DateField(verbose_name='Data pomiaru')),
                ('temp_measurment_time', models.TimeField(verbose_name='Czas poiaru')),
                ('room_foreign_key', models.ForeignKey(to='show_temp.Place')),
            ],
        ),
    ]
