# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_auto_20160122_1447'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articles',
            old_name='created',
            new_name='created_date',
        ),
        migrations.RenameField(
            model_name='articles',
            old_name='modified',
            new_name='modified_date',
        ),
    ]
