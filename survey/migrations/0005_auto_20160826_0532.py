# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0004_auto_20160826_0228'),
    ]

    operations = [
        migrations.AddField(
            model_name='survey',
            name='live',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='question',
            name='choices',
            field=models.TextField(help_text=b'Comma-separated list of choices/options.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='response',
            name='emailID',
            field=models.CharField(max_length=40, verbose_name=b'Email Address', blank=True),
        ),
        migrations.AlterField(
            model_name='response',
            name='interview_uuid',
            field=models.CharField(max_length=36, verbose_name=b'Survey unique identifier'),
        ),
        migrations.AlterField(
            model_name='response',
            name='interviewer',
            field=models.CharField(max_length=400, verbose_name=b'Name'),
        ),
    ]
