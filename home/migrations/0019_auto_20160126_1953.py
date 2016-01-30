# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_auto_20160125_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='content',
            field=tinymce.models.HTMLField(verbose_name=b'Article body'),
        ),
    ]
