# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20150616_2349'),
    ]

    operations = [
        migrations.AddField(
            model_name='plug',
            name='connected',
            field=models.BooleanField(default=False),
        ),
    ]
