# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('complaints', '0002_complaint_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='complaint',
            name='categoryId',
        ),
        migrations.AddField(
            model_name='complaint',
            name='emailid',
            field=models.CharField(max_length=40, blank=True),
        ),
        migrations.AddField(
            model_name='complaint',
            name='user_name',
            field=models.CharField(max_length=40, blank=True),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='category',
            field=models.CharField(blank=True, max_length=34, choices=[(b'Admit', b'admit'), (b'Staff', b'staff'), (b'Facilities', b'facilities'), (b'Other', b'other')]),
        ),
    ]
