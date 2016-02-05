# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0016_puesto_departamento'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='salario_actual',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='empleado',
            name='salario_contratacion',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='puesto',
            name='salario_maximo_inicial',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='puesto',
            name='salario_minimo_inicial',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
