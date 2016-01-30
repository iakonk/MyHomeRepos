# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_auto_20160125_1210'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articles',
            name='_body_rendered',
        ),
        migrations.RemoveField(
            model_name='articles',
            name='body',
        ),
        migrations.AlterField(
            model_name='articles',
            name='content',
            field=tinymce.models.HTMLField(verbose_name=b'Article body'),
        ),
    ]
