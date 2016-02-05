# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0009_archivo_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archivo',
            name='empleado',
            field=models.ForeignKey(to='empleados.Empleado'),
        ),
    ]
