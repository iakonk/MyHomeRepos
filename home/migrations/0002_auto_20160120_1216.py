# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import markitup.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='_article_body_rendered',
            field=models.TextField(editable=False, blank=True),
        ),
        migrations.AlterField(
            model_name='articles',
            name='article_body',
            field=markitup.fields.MarkupField(no_rendered_field=True),
        ),
    ]
