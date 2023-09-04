# Generated by Django 4.2.4 on 2023-08-31 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='registros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Codigo', models.CharField(max_length=7, unique=True)),
                ('Nombre', models.CharField(max_length=50)),
                ('Apellido_paterno', models.CharField(max_length=200)),
                ('Apellido_materno', models.CharField(max_length=200)),
                ('Fecha_nacimento', models.DateField()),
                ('Edad', models.IntegerField()),
                ('Email', models.CharField(max_length=50)),
                ('Telefono', models.CharField(max_length=9, unique=True)),
                ('Estado', models.IntegerField(choices=[[0, 'Activo'], [1, 'Inactivo']])),
            ],
        ),
    ]
