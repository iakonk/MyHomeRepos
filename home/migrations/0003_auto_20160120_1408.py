# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20160120_1216'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articles',
            old_name='_article_body_rendered',
            new_name='_body_rendered',
        ),
        migrations.RenameField(
            model_name='articles',
            old_name='article_body',
            new_name='body',
        ),
        migrations.RemoveField(
            model_name='articles',
            name='image',
        ),
        migrations.AddField(
            model_name='articles',
            name='header_image',
            field=models.ImageField(default='sdfds', upload_to=b'uploads/', verbose_name=b'Image header'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='articles',
            name='negative_feedback',
            field=models.IntegerField(default=0, verbose_name=b'Negative Feedback count'),
        ),
        migrations.AddField(
            model_name='articles',
            name='positive_feedback',
            field=models.IntegerField(default=0, verbose_name=b'Positive Feedback count'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'Date publichsed'),
        ),
    ]
