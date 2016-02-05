# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0008_auto_20151222_1656'),
    ]

    operations = [
        migrations.AddField(
            model_name='archivo',
            name='nombre',
            field=models.CharField(default=1, max_length=140),
            preserve_default=False,
        ),
    ]
