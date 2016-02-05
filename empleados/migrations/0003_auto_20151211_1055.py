# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0002_auto_20151209_0935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='celular',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='empleado',
            name='departamento',
            field=models.ForeignKey(default=1, to='empleados.Departamento'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='empleado',
            name='puesto',
            field=models.ForeignKey(default=1, to='empleados.Puesto'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='empleado',
            name='telefono',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
    ]
