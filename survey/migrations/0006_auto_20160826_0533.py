# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0005_auto_20160826_0532'),
    ]

    operations = [
        migrations.RenameField(
            model_name='survey',
            old_name='live',
            new_name='is_live',
        ),
    ]
