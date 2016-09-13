# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0006_auto_20160826_0533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survey',
            name='description',
            field=models.CharField(max_length=255),
        ),
    ]
