# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='appliance',
            table='appliance',
        ),
        migrations.AlterModelTable(
            name='plug',
            table='plug',
        ),
        migrations.AlterModelTable(
            name='residence',
            table='residence',
        ),
        migrations.AlterModelTable(
            name='usage',
            table='usage',
        ),
    ]
