# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20160120_1408'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='article_type',
            field=models.CharField(default=b'M', max_length=2, verbose_name=b'Article type', choices=[(b'M', b'Monitoring'), (b'V', b'Visualizing'), (b'P', b'Provisioning'), (b'N', b'Networking'), (b'W', b'Web-solutions'), (b'D', b'Deployment'), (b'O', b'Other')]),
        ),
        migrations.AlterField(
            model_name='articles',
            name='header_image',
            field=models.ImageField(upload_to=b'/root/MyHomeRepos/conda/uploads/', verbose_name=b'Image header'),
        ),
    ]
