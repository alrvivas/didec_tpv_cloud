# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0005_auto_20151222_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='imagen',
            field=models.ImageField(upload_to=b'images/categorias', null=True, verbose_name=b'Imagen Categoria', blank=True),
        ),
    ]
