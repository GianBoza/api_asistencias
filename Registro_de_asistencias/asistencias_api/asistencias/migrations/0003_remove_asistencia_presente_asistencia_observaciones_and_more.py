# Generated by Django 5.1.4 on 2025-01-03 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asistencias', '0002_asistencia_hora_entrada_asistencia_hora_salida'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asistencia',
            name='presente',
        ),
        migrations.AddField(
            model_name='asistencia',
            name='observaciones',
            field=models.TextField(blank=True, null=True, verbose_name='Observaciones'),
        ),
        migrations.AlterField(
            model_name='asistencia',
            name='fecha',
            field=models.DateField(verbose_name='Fecha de asistencia'),
        ),
        migrations.AlterField(
            model_name='asistencia',
            name='hora_entrada',
            field=models.TimeField(blank=True, null=True, verbose_name='Hora de entrada'),
        ),
        migrations.AlterField(
            model_name='asistencia',
            name='hora_salida',
            field=models.TimeField(blank=True, null=True, verbose_name='Hora de salida'),
        ),
        migrations.AlterField(
            model_name='asistencia',
            name='nombre',
            field=models.CharField(max_length=100, verbose_name='Nombre del empleado'),
        ),
    ]
