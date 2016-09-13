# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='response',
            name='interviewee',
        ),
        migrations.AlterField(
            model_name='response',
            name='emailID',
            field=models.CharField(max_length=400, verbose_name=b'emailID'),
        ),
    ]
