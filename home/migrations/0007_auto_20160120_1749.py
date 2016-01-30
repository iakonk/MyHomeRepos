# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20160120_1737'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='slug',
            field=models.SlugField(default='dfhh', verbose_name=b'Slug'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='articles',
            name='header',
            field=models.TextField(verbose_name=b'Header'),
        ),
    ]
