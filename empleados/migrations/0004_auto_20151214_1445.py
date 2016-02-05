# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0003_auto_20151211_1055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='departamento',
            field=models.ForeignKey(to='empleados.Departamento', null=True),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='puesto',
            field=models.ForeignKey(to='empleados.Puesto', null=True),
        ),
    ]
