# Generated by Django 4.1.1 on 2022-09-20 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pacientes',
            fields=[
                ('id_paciente', models.AutoField(primary_key=True, serialize=False)),
                ('genero', models.CharField(max_length=20, verbose_name='genero')),
                ('nombres', models.CharField(max_length=45, verbose_name='Nombre completo')),
                ('tipoDocumento', models.CharField(max_length=20, verbose_name='tipo documento')),
                ('numeroDocument0', models.CharField(max_length=30, verbose_name='numero de documento')),
                ('telefono', models.CharField(max_length=25, verbose_name='numero celular')),
                ('direccion', models.CharField(max_length=45, verbose_name='direccion')),
                ('ciudad', models.CharField(max_length=25, verbose_name='Ciudad')),
            ],
        ),
    ]
