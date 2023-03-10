# Generated by Django 4.1.7 on 2023-02-23 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='autor',
            options={'ordering': ['id'], 'verbose_name': 'Autor', 'verbose_name_plural': 'Autores'},
        ),
        migrations.AlterField(
            model_name='autor',
            name='apellidos',
            field=models.CharField(max_length=200, verbose_name='Apellidos'),
        ),
        migrations.AlterField(
            model_name='autor',
            name='descripcion',
            field=models.CharField(max_length=200, verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='autor',
            name='nacionalidad',
            field=models.CharField(max_length=100, verbose_name='Nacionalidad'),
        ),
        migrations.AlterField(
            model_name='autor',
            name='nombre',
            field=models.CharField(max_length=200, verbose_name='Nombres'),
        ),
    ]
