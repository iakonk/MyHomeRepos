# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_articles_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='content',
            field=models.TextField(),
        ),
    ]
