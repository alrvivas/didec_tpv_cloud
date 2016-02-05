# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0010_auto_20151222_1803'),
    ]

    operations = [
        migrations.AddField(
            model_name='departamento',
            name='descripcion',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
