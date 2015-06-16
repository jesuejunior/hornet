# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appliance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=55)),
                ('type', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Plug',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=55)),
                ('room', models.TextField()),
                ('appliance', models.ForeignKey(blank=True, to='api.Appliance', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Residence',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cep', models.CharField(max_length=7)),
                ('address', models.CharField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Usage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('registered', models.DateTimeField(auto_now_add=True)),
                ('value', models.FloatField()),
                ('plug', models.ForeignKey(to='api.Plug')),
            ],
        ),
    ]
