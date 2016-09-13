# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('complaints', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaint',
            name='category',
            field=models.CharField(default=b'M', max_length=34, choices=[(b'M', b'Male'), (b'F', b'Female')]),
        ),
    ]
