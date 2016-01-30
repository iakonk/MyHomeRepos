# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_auto_20160121_2004'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articles',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='articles',
            name='slug',
        ),
        migrations.AddField(
            model_name='articles',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 22, 14, 46, 50, 335811, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='articles',
            name='modified',
            field=models.DateTimeField(default=2004, auto_now=True),
            preserve_default=False,
        ),
    ]
