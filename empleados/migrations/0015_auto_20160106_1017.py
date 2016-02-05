# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0014_puesto_perfil'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='escolaridad',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='empleado',
            name='estado_civil',
            field=models.CharField(max_length=150),
        ),
    ]
