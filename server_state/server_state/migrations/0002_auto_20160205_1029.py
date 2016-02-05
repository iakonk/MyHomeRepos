# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('server_state', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='serverstate',
            name='normal_work',
        ),
        migrations.RemoveField(
            model_name='serverstate',
            name='server_off',
        ),
        migrations.RemoveField(
            model_name='serverstate',
            name='server_on',
        ),
        migrations.AddField(
            model_name='serverstate',
            name='state',
            field=models.CharField(default=b'NORMAL', max_length=10, verbose_name=b'Current state', choices=[(b'NORMAL', b'Server normal work'), (b'OFF', b'Shutdown server'), (b'ON', b'Boot server')]),
        ),
    ]
