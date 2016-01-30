# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_auto_20160122_1507'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='content',
            field=tinymce.models.HTMLField(default=''),
            preserve_default=False,
        ),
    ]
