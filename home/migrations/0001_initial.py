# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name=b'Date created')),
                ('header', models.SlugField(verbose_name=b'Article Header')),
                ('article_body', models.TextField(verbose_name=b'Article text')),
                ('image', models.ImageField(upload_to=b'uploads/', verbose_name=b'Images storage')),
            ],
        ),
    ]
