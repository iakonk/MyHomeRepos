# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20160120_1822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='article_type',
            field=models.CharField(default=b'M', max_length=2, verbose_name=b'Article type', choices=[(b'M', b'Monitoring'), (b'V', b'Visualizing'), (b'P', b'Provisioning'), (b'N', b'Networking'), (b'W', b'Web'), (b'D', b'Deployment'), (b'O', b'Other')]),
        ),
    ]
