# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0007_archivos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Archivo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('archivo', models.FileField(upload_to=b'archivos/categorias', null=True, verbose_name=b'Imagen Categoria', blank=True)),
                ('empleado', models.OneToOneField(to='empleados.Empleado')),
            ],
        ),
        migrations.RemoveField(
            model_name='archivos',
            name='empleado',
        ),
        migrations.DeleteModel(
            name='Archivos',
        ),
    ]
