# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0015_auto_20160106_1017'),
    ]

    operations = [
        migrations.AddField(
            model_name='puesto',
            name='departamento',
            field=models.ForeignKey(to='empleados.Departamento', null=True),
        ),
    ]
