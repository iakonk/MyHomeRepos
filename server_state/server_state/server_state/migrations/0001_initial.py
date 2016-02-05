# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ServerState',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('normal_work', models.BooleanField(default=False, verbose_name=b'Normal work')),
                ('server_on', models.BooleanField(default=False, verbose_name=b'Start server')),
                ('server_off', models.BooleanField(default=False, verbose_name=b'Shutdown server')),
            ],
        ),
    ]
