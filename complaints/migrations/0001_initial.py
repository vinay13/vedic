# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=233, blank=True)),
                ('body', models.TextField()),
                ('categoryId', models.CharField(max_length=12, blank=True)),
            ],
        ),
    ]
