# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0013_auto_20160102_1411'),
    ]

    operations = [
        migrations.AddField(
            model_name='puesto',
            name='perfil',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
