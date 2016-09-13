# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0003_remove_response_emailid'),
    ]

    operations = [
        migrations.AddField(
            model_name='response',
            name='emailID',
            field=models.CharField(max_length=40, blank=True),
        ),
        migrations.AlterField(
            model_name='response',
            name='interviewer',
            field=models.CharField(max_length=400, verbose_name=b'EmailID'),
        ),
    ]
