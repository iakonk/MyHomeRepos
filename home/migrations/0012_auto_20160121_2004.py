# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_articles_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='header_image',
            field=easy_thumbnails.fields.ThumbnailerImageField(upload_to=b'/uploads/', verbose_name=b'Image header'),
        ),
    ]
