# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0012_contrato'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actas_Administrativas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.TextField()),
                ('archivo', models.FileField(upload_to=b'archivos/categorias', null=True, verbose_name=b'Acta Administrativa', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Periodo_Vacaional',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.TextField()),
                ('fecha_inicio', models.DateField(null=True)),
                ('fecha_fin', models.DateField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name='empleado',
            name='curp',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='empleado',
            name='edad',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='empleado',
            name='estado_civil',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='empleado',
            name='fecha_ingreso',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='empleado',
            name='numero_seguridad_social',
            field=models.CharField(default=1, max_length=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='empleado',
            name='preparacion_academica',
            field=models.CharField(default=1, max_length=140),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='empleado',
            name='rfc',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='empleado',
            name='tipo_contrato',
            field=models.ForeignKey(to='empleados.Contrato', null=True),
        ),
        migrations.AlterField(
            model_name='archivo',
            name='archivo',
            field=models.FileField(upload_to=b'archivos/categorias', null=True, verbose_name=b'Archivos', blank=True),
        ),
        migrations.AddField(
            model_name='periodo_vacaional',
            name='empleado',
            field=models.ForeignKey(to='empleados.Empleado'),
        ),
        migrations.AddField(
            model_name='actas_administrativas',
            name='empleado',
            field=models.ForeignKey(to='empleados.Empleado'),
        ),
    ]
