# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('server_state', '0002_auto_20160205_1029'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='serverstate',
            name='state',
        ),
        migrations.AddField(
            model_name='serverstate',
            name='current_state',
            field=models.CharField(default=b'NORMAL', max_length=10, verbose_name=b'Current state', choices=[(b'NORMAL', b'Schedule server normal'), (b'OFF', b'Schedule server shutdown'), (b'ON', b'Schedule server boot')]),
        ),
        migrations.AddField(
            model_name='serverstate',
            name='last_updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
