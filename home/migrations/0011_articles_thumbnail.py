# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20160121_1533'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='thumbnail',
            field=easy_thumbnails.fields.ThumbnailerImageField(default=1, upload_to=b'/uploads/', verbose_name=b'Thumbnail'),
            preserve_default=False,
        ),
    ]
