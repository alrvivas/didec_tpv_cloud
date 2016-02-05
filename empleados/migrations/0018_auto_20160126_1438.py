# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0017_auto_20160106_1033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='celular',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='curp',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='direccion',
            field=models.CharField(max_length=140, null=True),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='escolaridad',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='estado_civil',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='numero_seguridad_social',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='preparacion_academica',
            field=models.CharField(max_length=140, null=True),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='rfc',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='telefono',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
