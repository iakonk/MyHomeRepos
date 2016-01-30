# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20160120_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='header_image',
            field=models.ImageField(upload_to=b'/uploads/', verbose_name=b'Image header'),
        ),
    ]
