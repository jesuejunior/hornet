# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_plug_connected'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usage',
            old_name='value',
            new_name='total_usage',
        ),
        migrations.AddField(
            model_name='plug',
            name='priority',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='usage',
            name='kilowatt_hour',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usage',
            name='power',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usage',
            name='voltage',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
