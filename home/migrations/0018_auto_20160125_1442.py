# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_auto_20160125_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='content',
            field=tinymce.models.HTMLField(max_length=1000, verbose_name=b'Article body'),
        ),
    ]
