# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0018_auto_20160126_1438'),
    ]

    operations = [
        migrations.AddField(
            model_name='periodo_vacaional',
            name='titulo',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='periodo_vacaional',
            name='descripcion',
            field=models.TextField(null=True),
        ),
    ]
