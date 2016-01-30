# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20160120_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='header',
            field=models.SlugField(max_length=100, verbose_name=b'Article Header'),
        ),
    ]
